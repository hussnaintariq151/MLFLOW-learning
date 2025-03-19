import mlflow
import dagshub

# Initialize DagsHub MLflow tracking
dagshub.init(repo_owner="hussnaintariq151", repo_name="MLFLOW-learning", mlflow=True)

# Check tracking URI
print("Tracking URI:", mlflow.get_tracking_uri())
