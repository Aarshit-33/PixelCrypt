from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import hideLossy
import hide_lossless

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    if request.method == 'POST':
        # Get image from the front end 
        file = request.files['input_image']
        # Create path for new folder to save image data.
        # Avoid creating folder of same name again if user uploads image with same name 
        # because it will generate an OS error 
        try:
            parent_dir = "static/data"
            filename = secure_filename(file.filename)
            path = os.path.join(parent_dir, filename[:-4])  
            os.mkdir(path)
        except:
            filename = secure_filename(file.filename)
        finally:
            UPLOAD_FOLDER = f'static/data/{filename[:-4]}'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # get message and key
        message = request.form['message']
        key = request.form['key']
        img_path = path + "/" + filename 
        save_path_lossy = path + "/" + filename[:-4] + "_lossyEncoded"  + ".png"
        save_path_lossless = path + "/" + filename[:-4] + "_lossless"  + ".png"

        try:
            key = int(key)
        except: 
            key = 12345 # Default Key
            
        # Hide the message inside the image ..
        # Lossy encoding 
        hideLossy.encode(img_path, str(message),  save_path_lossy)
        # Lossless encoding 
        hide_lossless.hide_data(int(key), str(message), save_path_lossless, img_path)

    return render_template('encode.html', original_image=img_path, lossy_encoded=save_path_lossy, lossless_encoded=save_path_lossless)




@app.route('/decode', methods=['POST'])
def decode():
    if request.method == 'POST':
        # Get image from the front end 
        file = request.files['input_image']
        # Create path for new folder to save image data.
        # Avoid creating folder of same name again if user uploads image with same name 
        # because it will generate an OS error 
        try:
            parent_dir = "static/to_decode"
            filename = secure_filename(file.filename)
            #path = os.path.join(parent_dir, filename[:-4])  
            #os.mkdir(path)
        except:
            filename = secure_filename(file.filename)
        finally:
            UPLOAD_FOLDER = f'static/to_decode'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        key = request.form['key']
        mode = request.form['message']
        image_path = parent_dir + "/" + filename 

        try:
            key = int(key)
        except: 
            key = 12345 # Default Key

        if "lossy" in filename:
            message = hideLossy.decode(image_path)
        elif "lossless" in filename:
            message = hide_lossless.retrieve_data(int(key), image_path)
    return render_template('decode.html', image_path=image_path, message=message)


if __name__ == '__main__':
    app.run(debug=True)
