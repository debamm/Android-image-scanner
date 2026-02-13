from pydantic import BaseModel, Field

#define the request and response schemas for the predict endpoint
#for image classification, request would include an image file
#response would include the predicted label and confidence score

class predict_request(BaseModel):
    image_url: str = Field(..., description="URL of the image to be classified")

    
class predict_response(BaseModel):
    label: str = Field(..., description="Predicted label for the input image")
    confidence: float = Field (..., description="Confidence score of the prediction")