import React, { Component } from 'react';
import Box from '@mui/material/Box';
import { DataGrid } from '@mui/x-data-grid';

export default class DataGridDemo extends Component {
    constructor() {
        super();
        this.state = {
            rows: [],
            columns: [],
        };
    }

    async componentDidMount() {
        let response = await fetch("https://jsonplaceholder.typicode.com/users");
        let data = await response.json();

        // Flatten the data structure
        const flattenedData = data.map((item) => ({
            id: item.id,
            name: item.name,
            username: item.username,
            email: item.email,
            phone: item.phone,
            website: item.website,
            'address.street': item.address?.street || '',
            'address.suite': item.address?.suite || '',
            'address.city': item.address?.city || '',
            'address.zipcode': item.address?.zipcode || '',
            'geo.lat': item.address?.geo?.lat || '',
            'geo.lng': item.address?.geo?.lng || '',
            'company.name': item.company?.name || '',
            'company.catchPhrase': item.company?.catchPhrase || '',
            'company.bs': item.company?.bs || '',
        }));

        // Generate columns dynamically
        const columns = Object.keys(flattenedData[0]).map((key) => ({
            field: key,
            headerName: key.toUpperCase(),
            width: 150,
            editable: true,
        }));

        this.setState({ rows: flattenedData, columns });
    }

    render() {
        const { rows, columns } = this.state;
        return (
            <Box sx={{ height: 600, width: '100%' }}>
                <DataGrid
                    rows={rows}
                    columns={columns}
                    initialState={{
                        pagination: {
                            paginationModel: {
                                pageSize: 5,
                            },
                        },
                    }}
                    pageSizeOptions={[5, 10, 20]}
                    checkboxSelection
                    disableRowSelectionOnClick
                />
            </Box>
        );
    }
}


