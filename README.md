# Hateful_means_dataset
This is meta Hateful means dataset and you can use it to fine-tune your vllm

Due this dataset is too large too upload by git

So only JSONL, which can be used to fine-tune,infer and evaluate your model

The whole dataset may be you can load from [here](https://hyper.ai/cn/datasets/17894)

you need to know that:

dev.jsonl train.jsonl test.jsonl is offered by meta and others are all converted

here is the mean of all jsonl files

[dev.jsonl](JSONL/dev.jsonl):This is the initial test jsonl,which contains id, image, label, and test. You can use it to test your final model;

[train.jsonl](JSONL/train.jsonl):This is the initial train jsonl,which contains id, image, label, and test. You can use it train your model;

[test.jsonl](JSONL/test.jsonl):This is the initial test jsonl,which contains id, image, and test. Attention! The labels are not added. So you may use it test your model OCR ability;

And for myself, the train contain three stage

First, I only fine-tuned OCR model, you can use [train_OCR.jsonl](JSONL/train_OCR.jsonl), [test_OCR_convert.jsonl](test_OCR_convert/test.jsonl) to achieve this goal

Second, I only fine-tuned Object Dection model, you can use [train_object_detection.jsonl](JSONL/train_object_detection.jsonl), [dev_OD.jsonl](JSONL/dev_OD.jsonl) to achieve this goal

Last, I fine-tuned a model which contain OCR and Object Dection ability, you can use [train_together.jsonl](JSONL/train_together.jsonl), [dev_test_OCR_OD.jsonl](JSONL/dev_test_OCR_OD.jsonl) to achieve this goal

You may can use [OCR_OD_infer](JSONL/OCR_OD_infer) to infer and evaluate your model.

If you want other type of JSONL, the [convert.py](./convert.py) may helpful for you
