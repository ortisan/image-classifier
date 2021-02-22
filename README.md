## Image Classifier

Label your images.

You need provides an json with the schema:

```json
{
    type: string, // Used to title your classification
    labels: [string], // Possible image labels
    data: [
        {
            id: string // Image id
            name: string // Image name
            label: string // Empty string. After classification we will fill this field
            features: {} // Features to use later on ML algo.
        }]
}
```

### Environment

1. Run commands:

   ```sh
   conda create -n image_classifier python=3.6.12
   conda activate image_classifier
   pip install -r requirements.txt
   ```

1. Start server

   ```sh
   python manage.py runserver
   ```

1. Run your classifier: http://localhost:8000/classifier


### Analysis:

1. Run your analysis:
   ```sh
   jupyter notebook notebooks
   ```
2. Example:
   **[CandleStickClassification.ipynb](https://github.com/tentativafc/image-classifier/blob/main/notebooks/CandleStickClassification.ipynb)**

### TODO

UX like Recaptcha.