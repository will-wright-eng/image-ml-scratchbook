# image-ml-scratchbook

## dev notes

```bash
export CONDA_NAME=image-ml-scratchbook
conda create -n "$CONDA_NAME" python=3.11 -y
conda activate "$CONDA_NAME"
python -m pip install replicate
python -m pip freeze > requirements.txt
```

`aws s3 cp myimages.zip s3://<bucket>/myimages.zip`

```bash
bash train-dreambooth-myimages.sh
```

```js
{"created_at":"2023-04-17T07:37:12.067340Z",
	"error":null,
	"id":"ngyq3ezzrvcjthbzficakaiww4",
	"input":{
		"class_prompt":"a photo of a person",
		"instance_data":"https://<bucket>/myimages.zip",
		"instance_prompt":"a photo of a cjw person",
		"max_train_steps":2000
	},
	"logs":null,
	"metrics":{},
	"model":"dummy-work-account/yourmodel",
	"notes":null,
	"status":"queued",
	"webhook_completed":"https://example.com/dreambooth-webhook",
	"version":null
}
````

### docker example setup

```bash
FROM python:3.9-slim-buster

ENV MY_VAR=my_value

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "my_script.py" ]
```

```bash
docker run -it <image_name> /bin/zsh
docker run -it --rm --name mycontainer -e MYARG=myvalue myimage:tag
```

## link dump

- [The Pet Painting - AI Pet Art](https://thepetpainting.com/)
- [google/dreambooth](https://github.com/google/dreambooth)
- [Train and deploy a DreamBooth model on Replicate - Replicate – Replicate](https://replicate.com/blog/dreambooth-api)
- [Run a model from Python – Replicate](https://replicate.com/docs/get-started/python)
- [How I Used Stable Diffusion and Dreambooth to Create A Painted Portrait of My Dog - In this post, we walk through my entire workflow/process for bringing Stable Diffusion to life as a high-quality framed art print. We’ll touch on making art with Dreambooth, Stable Diffusion, Outpainting, Inpainting, Upscaling, preparing for print with Photoshop, and finally printing on fine-art paper with an Epson XP-15000 printer.](https://www.shruggingface.com/blog/how-i-used-stable-diffusion-and-dreambooth-to-create-a-painted-portrait-of-my-dog)
- [Making Self Portraits With Stable Diffusion and LoRA - In this post, we walk through making self portraits with Stable Diffusion and LoRA](https://www.shruggingface.com/blog/self-portraits-with-stable-diffusion-and-lora)

## link dump 20230418

- [AUTOMATIC1111/stable-diffusion-webui: Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/tree/master)
- [HTTP API reference – Replicate](https://replicate.com/docs/reference/http#models.versions.list)
- [Run a model from Python – Replicate](https://replicate.com/docs/get-started/python)
- [replicate/dreambooth – API reference](https://replicate.com/replicate/dreambooth/api)
- [Train and deploy a DreamBooth model on Replicate - Replicate – Replicate](https://replicate.com/blog/dreambooth-api)
- [How I Used Stable Diffusion and Dreambooth to Create A Painted Portrait of My Dog - In this post, we walk through my entire workflow/process for bringing Stable Diffusion to life as a high-quality framed art print. We’ll touch on making art with Dreambooth, Stable Diffusion, Outpainting, Inpainting, Upscaling, preparing for print with Photoshop, and finally printing on fine-art paper with an Epson XP-15000 printer.](https://www.shruggingface.com/blog/how-i-used-stable-diffusion-and-dreambooth-to-create-a-painted-portrait-of-my-dog)
- [Making Self Portraits With Stable Diffusion and LoRA - In this post, we walk through making self portraits with Stable Diffusion and LoRA](https://www.shruggingface.com/blog/self-portraits-with-stable-diffusion-and-lora)
- [RedPajama, a project to create leading open-source models, starts by reproducing LLaMA training dataset of over 1.2 trillion tokens — TOGETHER](https://www.together.xyz/blog/redpajama)
