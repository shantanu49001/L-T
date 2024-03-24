import React, { useState } from 'react';
import './MaterialAdmin.css';
import axios from 'axios';
import imageSrc from '../Login/logo.png'; // Import your image file

const ImageMatchingForm = () => {
    const [selectedImage, setSelectedImage] = useState(null);
    const [matchPercentage, setMatchPercentage] = useState('');

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        setSelectedImage(file);
    };

    const handleMatch = async () => {
        var match = 10;
        try {
            // const response = await axios.post('http://localhost:5000/login', { name: "a", email: "acvx@g.com", password: 12345678, role: "a" });
            const response = await axios.get(' http://10.1.5.145:3080/my_function', { params: { name: "a" } });

            if (response.status === 200) {
                console.log(response);
                match = response.data.percentage;
            } else {
                console.error('Login failed');
                // Handle login failure
            }
        } catch (error) {
            console.error('Error:', error);
        }
        const randomMatchPercentage = match;
        setMatchPercentage(randomMatchPercentage + '%');
    };

    return (
        <div className="image-matching-container">
            <div className="image-container">
                <img src={imageSrc} alt="Image" />
            </div>
            <h2>Sand Quality Matching</h2>
            <div className="form-group">
                <label form='photo'>Select an image:</label>
                <input
                    type="file"
                    accept="image/*"
                    id="photo"
                    name="photo"
                    onChange={handleImageChange}
                />
            </div>
            <button onClick={handleMatch}>Match</button>
            {matchPercentage && (
                <div className="match-result">
                    <p>Match Percentage: {matchPercentage}</p>
                </div>
            )}
            <footer className="footer">
                <p className="footer-text">
                    This feature can be extended to measuring lengths via image and detecting cracks on commodities via OpenCV algorithms.
                </p>
            </footer>
        </div>
    );
};

export default ImageMatchingForm;
