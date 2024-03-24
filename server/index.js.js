//dev 
const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
//db 
const mongoose = require('mongoose');
const Admin = require('./models/usermodel');
const multer = require('multer');


const multerStorage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, `public/images`);
    }
    ,
    filename: (req, file, cb) => {
        const ext = file.mimetype.split('/')[1];
        cb(null, `1.${ext}`);
    }
}
)

const upload = multer({ storage: multerStorage });
//middle ware 
const app = express();

dotenv.config({ path: './config.env' });
app.use(cors());
app.use(express.json());  //convert every req to json object 

//db connection eshtablish 
mongoose.connect(process.env.DATABASE_LOCAL).then(con => {
    //console.log(con); //connection sucessfull
})

//muter_config 


//endpoints
app.get(`/api`, (req, res) => {
    console.log(req.body);
    res.json({ "users": ["user1", "user2"] });
})



//image processing 
app.get(`/material_match`, upload.single('photo'), async (req, res) => {
    console.log(req.params);
    //console.log(req.file.mimetype);
    res.status(200).json({
        status: 'sucess',
        percentage: 1700
    })
})

app.post(`/login`, async (req, res) => {

    const email = req.body.email;
    const password = req.body.password;
    const userObj = {
        name: req.body.name,
        email: req.body.email,
        password: req.body.password,
        role: req.body.role
    }
    console.log(req.body);
    await Admin.create(userObj);
    const user = await Admin.findOne({ email, password });
    console.log(user);
    if (user) {
        res.status(200).json({
            status: 200,
            message: "Done"
        })
    }
    else {
        res.status(404).json({
            status: 404,
            message: "failed"
        })
    }
})




//error handle for invalid req 
app.get(`*`, (req, res) => {
    res.json({
        status: 404,
        message: "Invalid req made no endpt to support"
    })
})
app.listen(5000, () => {
    console.log("Server on 5000");
})  //client 3000 pr 