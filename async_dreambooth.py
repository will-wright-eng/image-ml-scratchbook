import os
import random
from pprint import pprint
import uuid

import replicate
import requests
from dotenv import load_dotenv

load_dotenv()

class replicateApi:
    def __init__(self):
        self.username = 'dummy-work-account'
        self.model_name = 'yourmodel'
        self.model_slug = f'{self.username}/{self.model_name}'
        self.img_urls = []
        self.results = {}
        self.model = replicate.models.get(self.model_slug)
        self.versions = self.model.versions.list()

    async def generate_dreambooth_img(self, prompt):
        if not len(self.versions) == 1:
            raise ValueError('unexpected number of model versions')
        else:
            version = self.versions[0]
        negative_prompt = "blurry, deformed, watermark, dark lighting, image caption, low quality, low resolution, malformed, messy, blurry, watermark"
        image_urls = version.predict(
            prompt=prompt,
            width=512,
            height=512,
            negative_prompt=negative_prompt,
            num_outputs=4,
        )
        self.img_urls.append(image_urls)
        self.results[str(uuid.uuid4())] = {"prompt":prompt,"img_url_output":image_urls}

    def img_urls_from_results(self):
        self.img_urls = [resultdict.get('img_url_output', None) for resultid, resultdict in self.results.items()]

    def get_img_urls(self):
        if len(self.img_urls) == 0 and len(self.results) == 0:
            raise ValueError('no results present')
        elif len(self.img_urls) == 0:
            self.img_urls_from_results()
        return [item for sublist in self.img_urls for item in sublist]

    async def execute_prompt_list(self, prompt_list):
        random.shuffle(prompts)
        for prompt in prompts:
            print(prompt)
            await self.generate_dreambooth_img(prompt)
        print('\nprompt list complete\n')
        # pprint(self.results)

    def display_imgs(self, url):
        display(Image(url=url))

    def display_all_imgs(self):
        for url in self.get_img_urls():
            self.display_imgs(url)

    def download_img(self, url):
        filename = url.split('/')[-1]
        response = requests.get(url)
        pprint(dict(response.headers))

        if response.headers['Content-Type'] == 'image/png':
            with open(filename, 'wb') as f:
                f.write(response.content)
                print('Image downloaded successfully.')
                Image(filename=filename)
        else:
            print('The URL does not contain a PNG image.')
        pass


async def main():
	subject_id = "cjw"
	subject_noun = "happy male human"
	subject_gender = "his"
	# these prompts were all taken from [https://lexica.art/?q=dog+portrait](https://lexica.art/?q=dog+portrait)
	prompts = [
	    f"Adorably cute {subject_id} {subject_noun} portrait, artstation winner by Victo Ngai, Kilian Eng and by Jake Parker, vibrant colors, winning-award masterpiece, fantastically gaudy, aesthetic octane render, 8K HD Resolution",
	    f"Incredibly cute {subject_id} {subject_noun} portrait, artstation winner by Victo Ngai, Kilian Eng and by Jake Parker, vibrant colors, winning-award masterpiece, fantastically gaudy, aesthetic octane render, 8K HD Resolution",
	    f"a high quality painting of a very cute {subject_id} {subject_noun}, friendly, curious expression. painting by artgerm and greg rutkowski and alphonse mucha",
	    f"magnificent {subject_id} {subject_noun} portrait masterpiece work of art. oil on canvas. Digitally painted. Realistic. 3D. 8k. UHD.",
	    f"intricate five star {subject_id} {subject_noun} facial portrait by casey weldon, oil on canvas, hdr, high detail, photo realistic, hyperrealism, matte finish, high contrast, 3 d depth, centered, masterpiece, vivid and vibrant colors, enhanced light effect, enhanced eye detail, artstationhd ",
	    f"a portrait of a {subject_id} {subject_noun} in a scenic environment by mary beale and rembrandt, royal, noble, baroque art, trending on artstation ",
	    f"a painted portrait of a {subject_id} {subject_noun} with brown fur, no white fur, wearing a sea captain's uniform and hat, sea in background, oil painting by thomas gainsborough, elegant, highly detailed, anthro, anthropomorphic {subject_noun}, epic fantasy art, trending on artstation, photorealistic, photoshop, behance winner ",
	    f"{subject_id} {subject_noun} guarding {subject_gender} home, dramatic sunset lighting, mat painting, highly detailed, ",
	    f"{subject_id} {subject_noun}, realistic shaded lighting poster by ilya kuvshinov katsuhiro otomo, magali villeneuve, artgerm, jeremy lipkin and michael garmash and rob rey ",
	    f"a painting of a {subject_id} {subject_noun} {subject_noun}, greg rutkowski, cinematic lighting, hyper realistic painting",
	    f"painting of {subject_id} by andy warhol",
	    f"abstract impressionist portrate of {subject_id}",
	    f"cartoon portrait of {subject_id} facial, high definition, happy",
	]

	api = replicateApi()
	await api.execute_prompt_list(prompt_list=prompts)

if __name__ == "__main__":
	asyncio.run(main())
