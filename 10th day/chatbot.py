from flask import Flask
from langchain_core.tools import tool
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import *
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import * 
from langchain.agents.tool_calling_agent.base import create_tool_calling_agent
from  langchain.agents.agent import AgentExecutor
import pprint
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime, time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
db = SQLAlchemy(app)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prompt = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    

    def __repr__(self):
        return '<Messages %r>' % self.title

# Create the database
with app.app_context():
    db.create_all()

memory = InMemoryChatMessageHistory(session_id="test-session")


model = ChatMistralAI(
    model="open-mistral-nemo",
    temperature=0,
    max_retries=2,
)

@tool 
def add(a:int, b:int) -> int:
    """adds a and b"""
    return a + b 
    
@tool 
def multiply(a:int, b:int) -> int:
    """multiply a and b"""
    return a * b 
    
tools = [add, multiply]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    
    ('placeholder', "{chat_history}"),
    ('human', "{query}"),
   
    ('placeholder', "{agent_scratchpad}"),
    ])
    
    
agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

agent_history = RunnableWithMessageHistory(
    agent_executor,
    
    lambda session_id: memory,
    input_messages_key="query",
    history_messages_key="chat_history",
)


conf = {"configurable": {"session_id" : "test-session"}}

@app.route('/', methods= ['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form.get('message')  
        if message:
            query = dict(query=message)
            response = agent_history.invoke(query, conf)  
           
            print("Response:", response)
            
            time.sleep(2)

           
            if isinstance(response, dict) and 'output' in response:
                new_message = Messages(
                    prompt=message,  
                    message=response['output']  
                )
                db.session.add(new_message)
                db.session.commit()
            else:
                print("Error: Response does not have a valid output field")
                print("Response:", response)
        return redirect(url_for('share'))
    return render_template('home.html')





@app.route('/share', methods=["GET"])
def share():
    messages = Messages.query.all()
    return render_template('messages.html', messages = messages)
    

if __name__ =='__main__':
     app.run(debug=True)