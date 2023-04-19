# novel-cross-view-generation

## Data Prep
Download zip file into HD6. Download corresponding zip into GroundTruth folder. </p>
Generate tfrecord files.
```
viewformer-cli dataset generate --loader interiornet --path <path to tfrecord folder> --image-size 128 --output /home/ec2-user/novel-cross-view-generation/viewformer/dataset/interiornet/ --max-sequences-per-shard 50 --shuffle --split test 
```
Run inference script.
```
python3 demo.py --dataset_path <path to tfrecord folder> --query_env_path <path to environment folder you want to generate queries from> 
```
