# Architecture

The system follows clean boundaries: Flutter UI, FastAPI transport, domain services, SQLAlchemy persistence, and an AI pipeline interface. Video processing is isolated behind `FaceRecognitionPipeline` so local development can use CPU models while production can use GPU workers, queues, and vector indexes.
