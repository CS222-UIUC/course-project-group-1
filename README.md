

[![University of Illinois](https://img.shields.io/badge/University%20of%20Illinois-orange.svg)](https://illinois.edu)

# CleanSurf

___CleanSurf___ it is a web extension that allows for seamless filtering of explicit content to prevent such interactions and create a better overall browsing experience. The extension has a control panel where users can toggle the filter on and off, select how strict they want the filter to be, choose what type of content they want to filter, and customize the filter. 

## Developed With:

* [![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
* [![Django](https://img.shields.io/badge/Django-092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
* [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=javascript&logoColor=black)](https://www.javascript.com/)
* [![Google Chrome extension API](https://img.shields.io/badge/Google%20Chrome%20extension%20API-4285F4.svg?style=flat&logo=google-chrome&logoColor=white)](https://developer.chrome.com/extensions)
* [![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00.svg?style=flat&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
* [![NudeNet](https://img.shields.io/badge/NudeNet-pink.svg?style=flat&logo=github&logoColor=gray)](https://github.com/notAI-tech/NudeNet)


***
## Installation
<!-- create a list of steps to install the extension. Headlines in bold -->
1. #### Clone the repository
```bash
git clone https://github.com/CS222-UIUC/course-project-group-1.git
```
2. #### Install the dependencies
Make sure you have Python 3.9 or higher installed. Then, install the dependencies using the following command:
```bash
pip install -r requirements.txt
```
Make sure you have a chromium based browser installed.
3. #### Install nudeNet models
Models are located under the 'models' directory. To install the models, run the following command:
```bash
python models/install_models.py
```

***

## Usage
<!-- create a list of steps to use the extension. Headlines in bold -->
1. #### Run the server
```bash
python api/api.py
```
Note that the server is using port 5000 by default. If you want to change the port, you can do so by editing the `api/api.py` file.
2. #### Load the extension
    1. On your browser, go to `chrome://extensions/`
    2. Enable developer mode by toggling the switch in the top right corner (left panel if you are using Edge)
    3. Click on the `Load unpacked` button
    4. Navigate to the `extension` directory and select it
    5. Make sure the extension is enabled
3. #### Use the extension
    1. Navigate to any website
    2. Click on the extension icon
    3. Toggle the filter on by pressing the `CLEAN` button

***

