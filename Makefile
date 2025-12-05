deploy-test:
	gcloud functions deploy upload_image \
		--gen2 \
		--runtime=python312 \
		--region=asia-northeast1 \
		--source=. \
		--entry-point=upload_image \
		--trigger-http \
		--allow-unauthenticated \
		--project massive-house-480305-m8