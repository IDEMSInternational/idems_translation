# Translate Media Recorder JSON

Translate a JSON file to be uploaded to the Media Recorder. 

Set working directory to common_tools\media_recorder:
```
cd common_tools
cd media_recorder
```
Create output subfolder in media_recorder 

Run main.py script:
```
python main.py [dictionary] <input_file> [output_file]
```

- `dictionary` (mandatory). Dictionary relating source strings to their translations.
- `input_file` (mandatory). JSON file in source language that will be used as input. 
- `output_file` (mandatory). JSON file where the translated output will be saved. 


Example:
```
python main.py dictionary\example_dictionary.json input\example_input.json output\example_output.json
```