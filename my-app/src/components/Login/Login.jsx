import React, { useState } from 'react';
import './login.css';
import axios from 'axios';
import imageSrc from './logo.png'; // Import your image file
import MaterialAdmin from '../MaterialAdmin/MaterialAdmin';

var loggedIn = false;
var profile = "";
const LoginComponent = () => {
    const [selectedProfile, setSelectedProfile] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        try {
            const response = await axios.post('http://localhost:5000/login', { name: selectedProfile, email: email, password: password, role: selectedProfile });

            if (response.status === 200) {
                console.log('Login successful');
                // Redirect or perform further actions upon successful login
                loggedIn = true;
                profile = selectedProfile;
                //add link to 
            } else {
                console.error('Login failed');
                // Handle login failure
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(Number(e.target.value));
    };

    const handleProfileChange = (e) => {
        setSelectedProfile(e.target.value);
    };

    return (
        <div className="login-container">
            <img src={imageSrc} alt="Logo" className="rounded-image" /> {/* Add rounded image */}
            <h2>Login</h2>
            <div className="form-group">
                <label>Email:</label>
                <input
                    type="email"
                    value={email}
                    onChange={handleEmailChange}
                    placeholder="Enter your email"
                />
            </div>
            <div className="form-group">
                <label>Password:</label>
                <input
                    type="password"
                    value={password}
                    onChange={handlePasswordChange}
                    placeholder="Enter your password"
                />
            </div>
            <div className="profile-options">
                <label>
                    <input
                        type="radio"
                        value="manufacturer"
                        checked={selectedProfile === 'manufacturer'}
                        onChange={handleProfileChange}
                    />
                    Manufacturer
                </label>
                <label>
                    <input
                        type="radio"
                        value="shippingAdmin"
                        checked={selectedProfile === 'shippingAdmin'}
                        onChange={handleProfileChange}
                    />
                    Shipping Admin
                </label>
                <label>
                    <input
                        type="radio"
                        value="materialAdmin"
                        checked={selectedProfile === 'materialAdmin'}
                        onChange={handleProfileChange}
                    />
                    Material Admin
                </label>
            </div>
            <button onClick={handleLogin}>Login</button>
        </div>
    );
}


const LoginPage = () => {

    return <MaterialAdmin />;
};

export default LoginPage;