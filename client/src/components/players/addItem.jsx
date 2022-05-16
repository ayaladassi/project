import { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Routes, Route } from 'react-router-dom'
import React from 'react'
import ReactDOM from 'react-dom'


export default function AddItem(props) {
    return (
        <tr>
            <td scope="col">{props.Item.name}</td>
            <td scope="col">{props.Item.role}</td>
            <td scope="col">{props.Item.id}</td>
            <td scope="col">{props.Item.guid}</td>
            <td scope="col">{props.Item.color}</td>

        </tr>
    )
} 
