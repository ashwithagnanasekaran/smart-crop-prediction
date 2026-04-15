import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib  # Using joblib instead of pickle (better for large numpy arrays)
import warnings
warnings.filterwarnings('ignore')

# DATA PREPARATION
print("\n PREPARING DATA FOR MODELING...")

# Separate features and target
feature = df.drop(columns=['Crop'])
target = df['Crop']

print(f"   • Features shape: {feature.shape}")
print(f"   • Target shape: {target.shape}")
print(f"   • Features: {list(feature.columns)}")
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
target_encoded = le.fit_transform(target)

# TRAIN-TEST SPLIT
print("\n SPLITTING DATA...")
feature_train, feature_test, target_train, target_test = train_test_split(
    feature, target_encoded, test_size=0.2, random_state=42, stratify=target_encoded
)

print(f"   • Training set: {feature_train.shape[0]} samples")
print(f"   • Testing set: {feature_test.shape[0]} samples")
print(f"   • Stratified split: Yes (preserves crop distribution)")
# MODEL TRAINING
print("\n TRAINING XGBOOST MODEL...")

model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    use_label_encoder=False,
    eval_metric='mlogloss'
)

# Train the model
model.fit(feature_train, target_train)
print("    Model training complete!")
# Cross-validation
print("\n🔄 Performing 5-fold cross-validation...")
cv_scores = cross_val_score(model, feature, target_encoded, cv=5)
print(f"   • CV Accuracy: {cv_scores.mean()*100:.2f}% (+/- {cv_scores.std()*100:.2f}%)")
# MODEL EVALUATION
print("\n📊 EVALUATING MODEL PERFORMANCE...")

# Predictions
target_pred_encoded = model.predict(feature_test)
target_pred = le.inverse_transform(target_pred_encoded)
target_test_labels = le.inverse_transform(target_test)

# Accuracy
accuracy = accuracy_score(target_test_labels, target_pred)
print(f"\n✅ Test Accuracy: {accuracy * 100:.2f}%")

# Detailed classification report
print("\n📋 Classification Report:")
print("-"*60)
report = classification_report(target_test_labels, target_pred)
print(report)
# Confusion Matrix
print("\n📊 Generating Confusion Matrix...")
cm = confusion_matrix(target_test_labels, target_pred)
plt.figure(figsize=(12, 10))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=le.classes_, yticklabels=le.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
plt.show()
print("✅ Confusion matrix saved as 'confusion_matrix.png'")