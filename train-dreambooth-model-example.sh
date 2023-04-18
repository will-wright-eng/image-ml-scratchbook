#!/bin/bash

curl -X POST \
    -H "Authorization: Token $REPLICATE_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
            "input": {
                "instance_prompt": "a photo of a qdg dog",
                "class_prompt": "photograph of a golden retriever dog, 4k hd, high detail photograph, sharp lens, realistic, highly detailed, fur",
                "instance_data": "https://shruggyface.s3-us-west-2.amazonaws.com/queso-2023-transparent-all.zip",
                "max_train_steps": 4000
            },
            "model": "jakedahn/queso-1-5", # The dreambooth model will be added to your Replicate account at this URL. Replace "jakedahn" with your username...
            "trainer_version": "cd3f925f7ab21afaef7d45224790eedbb837eeac40d22e8fefe015489ab644aa",
            "webhook_completed": "https://abc123.m.pipedream.net/queso-1-5"
        }' \
    https://dreambooth-api-experimental.replicate.com/v1/trainings
