from flask import Flask, request,jsonify
#orm and ssim matrix method 
#we can use feaeture matching and template matching algos and then apply suitab;e colour channel selection to ensure better similarity 
from skimage.metrics import structural_similarity
import cv2
import numpy as np

def orb_sim(img1,img2):
    orb=cv2.ORB_create()

    #dect key point and descriptors
    kp_a,desc_a=orb.detectAndCompute(img1,None)
    kp_b,desc_b=orb.detectAndCompute(img2,None)

    #matcher object 
    bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

    #matches perform 
    matches=bf.match(desc_a,desc_b)
    similar_regions=[i for i in matches if i.distance<30] #scale down pixel distance diff for more precison
    if len(matches)==0:
        return 0 #no similar pixel 
    return len(similar_regions)/len(matches)  #probability of match 
#true +ves / total +ves [false and true ]
def structural_similarity(img1,img2):
    sim,diff=structural_similarity(img1,img2,full=True)
    return sim
img00=cv2.imread('b.png',0)  #we can modify colour channels tp focus on more details 
img01=cv2.imread('a.png',0)

orb_similarity=orb_sim(img00,img01)
print(img00)
print(img01)

print("Similarity %",orb_similarity*100)



app = Flask(__name__)

@app.route('/my_function', methods=['POST'])
def my_function():
    # Check if an image file is uploaded
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    # Access the uploaded image file
    image_file = request.files['image']

# Read the image data from the file object
    image_data = image_file.read()

    # Convert the image data to a NumPy array using OpenCV
    image_np_array = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

    # Process the image (for example, using the orb_sim function)
    # Note: Replace orb_sim with your actual image processing function
    result = orb_sim(image_np_array, img01)

    # Return the result
    return jsonify({'result': result*100})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3080)
