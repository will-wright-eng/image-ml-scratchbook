# image-ml-scratchbook

## dev notes

```bash
export CONDA_NAME=image-ml-scratchbook
conda create -n "$CONDA_NAME" python=3.11 -y
conda activate "$CONDA_NAME"

python -m pip install replicate
python -m pip freeze > requirements.txt
```

### docker example setup

```bash
docker run -it <image_name> /bin/zsh
docker run -it --rm --name mycontainer -e MYARG=myvalue myimage:tag
```

```bash
FROM python:3.9-slim-buster

ENV MY_VAR=my_value

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "my_script.py" ]
```

## link dump

- [The Pet Painting - AI Pet Art](https://thepetpainting.com/)
- [google/dreambooth](https://github.com/google/dreambooth)
- [Train and deploy a DreamBooth model on Replicate - Replicate – Replicate](https://replicate.com/blog/dreambooth-api)
- [Run a model from Python – Replicate](https://replicate.com/docs/get-started/python)
- [How I Used Stable Diffusion and Dreambooth to Create A Painted Portrait of My Dog - In this post, we walk through my entire workflow/process for bringing Stable Diffusion to life as a high-quality framed art print. We’ll touch on making art with Dreambooth, Stable Diffusion, Outpainting, Inpainting, Upscaling, preparing for print with Photoshop, and finally printing on fine-art paper with an Epson XP-15000 printer.](https://www.shruggingface.com/blog/how-i-used-stable-diffusion-and-dreambooth-to-create-a-painted-portrait-of-my-dog)
- [Making Self Portraits With Stable Diffusion and LoRA - In this post, we walk through making self portraits with Stable Diffusion and LoRA](https://www.shruggingface.com/blog/self-portraits-with-stable-diffusion-and-lora)
