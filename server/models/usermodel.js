const express = require('express');
const mongoose = require('mongoose');
const validator = require('validator');

const AdminSchema = new mongoose.Schema({
    name: {
        type: String
    },
    email: {
        type: String,
        required: [true, 'Please enter valid email'],
        validate: [validator.isEmail, 'Please enter a valid email']
    },
    role: {
        type: String,
        required: [true, 'Please enter valid role']
        // required: [true, 'Please enter valid role']
    },
    password: {
        type: String,
        required: [true, 'Please enter a valid password'],


    }
});
const Admin = mongoose.model('users', AdminSchema);
module.exports = Admin;