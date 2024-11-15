# Hateful_means_dataset
This is meta Hateful means dataset and you can use it to fine-tune your vllm

Due this dataset is too large too upload by git and i`am a free user

So I can not upload by LFS one time

I try to use split -b 100M dataset.tar.gz dataset_part_

and use the upload

so if you want to use and restore the dataset

you may need run 

git clone git@github.com:little-liu-little/Hateful_means_dataset.git

cd Hateful_means_dataset

cat dataset_part_* > dataset.tar.gz

tar -xzf dataset.tar.gz -C /path/to/your/dataset
