## Inspiration

After struggling to efficiently transcribe content during our fast-paced university lectures, our team realized that there was a lack of software available to accommodate physical notes in the digital age. We wanted to build a web-app that would seamlessly transfer material from soft to hard copy, and allow users to interact with learned content dynamically.

## What it does
Scribbit automatically transcribes (aka, "scribbs") pictures of handwritten notes using markup-inspired visual cues. Our program automatically organizes this input into a modular and dynamic work space. Here, users can further edit and interact with their displayed content in a visually intuitive manner.     

## How we built it
We used Google's Cloud Vision Machine Learning API for handwriting detection with OCR. Notes written using our markup-inspired formatting are processed using our algorithm into their respective containers. The modular workspace was created by combining quilljs and muuri's APIs for text-editing and drag-and-drop functionality.      

## Challenges we ran into
Given the extensive scope of our project, we struggled to connect the many moving parts of our code. Furthermore, it was difficult to implement and work with muuri's nested and dynamic containers. Lastly, interpreting and parsing the OCR output was tedious.

## Accomplishments that we're proud of
Our team worked together very efficiently to complete the many tasks. Furthermore, we were able to create a very unique product that required ample iterations of creative design.

## What we learned
We learned the value of teamwork and communication. Furthermore, given the many languages and API libraries involved with our project, we all were able to familiarize ourselves with new programming knowledge, from front-end and parsing to ML and OCR. 

## What's next for Scribbit
- Personalized handwriting recognition using trained machine learning models
- Natural language processing for video, definition, and related topic suggestions.  
- A more robust text editor (eg. bold, italics, underlining)
