
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from transformers import pipeline

class SummarizeBlogView(APIView):
    def post(self, request):
        try:
            blog_text = request.data.get("text", "")
            if not blog_text:
                return Response({"error": "No text provided"}, status=400)

            # Specify the model and revision explicitly
            summarizer = pipeline(
                "summarization",
                model="sshleifer/distilbart-cnn-12-6",  # Use a specific model
                revision="a4f8f3e",  # Specify the exact revision (ensure this is the desired version)
                framework="pt"  # Use PyTorch (this is fine if you're using a PyTorch-based model)
            )

            # Summarize the provided text
            summary = summarizer(blog_text, max_length=100, min_length=30, do_sample=False)

            return Response({"summary": summary[0]['summary_text']}, status=200)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
