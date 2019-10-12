# qSeeFood
This was done for 2019 QisKit Hackathon in Singapore, Center of Quantum Technologies. 

## Motivations
This is inspired by the Silicon Valley series fracas, See Food. Now we're tryingto create a quantum version of the binary classification algorithm.

## Quickstart
To use the notebook you will need to create a `secret.py` file containing the following content.

```
# in secret.py

TOKEN = '<INSERT IBM Q EXPERIENCE TOKEN HERE>'
```

Next you will need to install the dependencies and you should be able to run the notebook. You might want to use a virtual environment for this. If you are experiencing problems with tensorflow installation you should use anaconda.
```
pip install -r requirements.txt
```

## Overview
- The key findings of the qSeeFood experiment are split into two notebooks `qSeeFood` and `qSeeFood2`. 

- Relevant data are found in `./data` these are hot dog/not hot dog images obtained from [kaggle](https://www.kaggle.com/dansbecker/hot-dog-not-hot-dog)

- `hackathon-singapore-19.ipynb` contains starter code for the hackathon

In `qSeeFood` we did a cursory survey with MNIST and quickly realized that this was a pretty dumb idea. We compared the Quantum SVM with the Classical SVM and realized that the Classical SVM is better at classification as compared to the Quantum SVM. Due to time constraints we had to use a very small dataset, so the findings might not be really indicative of anything. The Classical SVM runs much faster compared to the simulated Quantum SVM so as of now there's no real reason to use a Quantum SVM for anything practical.

In `qSeeFood2` we YOLO'ed and just used the quantum SVM on the hotdog dataset for the lulz and got dismal results.

## Conclusion
Quantum Machine Learning is still very much in it's infancy. Without quantum RAM and more qubits it's unlike for Quantum Machine Learning approaches to rival Classical Machine Learning approaches. 

