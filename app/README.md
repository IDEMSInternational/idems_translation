# ParentApp-translation

## Running the scripts

Several JSON files must be accumulated into fewer JSON files by the 'compose' script, before the 'extract' script can be run.

### Compose JSON files

```
python scripts/compose_json_files.py input_dir output_dir
```

Where:

- `input_dir` is the directory where JSON files will be read from
- `output_dir` is the directory where JSON files will be saved to

### Extract texts

Copy data_lists, globals, templates and tours into the input folder. 

Change directory to app.

Generate JSON files for translation:
```
python scripts/extract_texts_script.py
```

Output will be saved in the `output` folder.

## Running the tests

```
python -m unittest scripts.tests
```
