#!/bin/bash

set -eo pipefail

source .env

curl -X POST \
    -H "Authorization: Token $REPLICATE_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
            "input": {
                "instance_prompt": "a photo of a cjw person",
                "class_prompt": "a photo of a person",
                "instance_data": "'"$SERVING_URL"'",
                "max_train_steps": 2000
            },
            "model": "dummy-work-account/yourmodel",
            "trainer_version": "cd3f925f7ab21afaef7d45224790eedbb837eeac40d22e8fefe015489ab644aa",
            "webhook_completed": "https://example.com/dreambooth-webhook"
        }' \
    https://dreambooth-api-experimental.replicate.com/v1/trainings
