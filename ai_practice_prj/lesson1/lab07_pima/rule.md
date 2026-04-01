# 📋 RULE.MD - QUY TẮC CHUẨN HOÀN TOÀN CHO DỰ ÁN MACHINE LEARNING

---

## 1️⃣ CẤU TRÚC BÀI LÀM (STRUCTURE)

### ✅ Thứ tự Các Phần (Mandatory Order):

- [ ] **Section 1: Define Problem** - Mô tả vấn đề, đầu vào, đầu ra, loại bài toán
- [ ] **Section 2: Prepare Problem** - Load libraries + Load dataset
- [ ] **Section 3: Exploration Analyze Data (EDA)** - Descriptive Statistics + Visualizations
- [ ] **Section 4: Data Preprocessing** - Clean + Transform (encoding, scaling)
- [ ] **Section 5: Data Splitting** - Train/Test split (7/3 hoặc 8/2)
- [ ] **Section 6: Model Building** - Build multiple models
- [ ] **Section 7: Model Evaluation** - Accuracy, Confusion Matrix, Cross-validation
- [ ] **Section 8: Parameter Tuning** - GridSearch/RandomSearch (nếu cần)
- [ ] **Section 9: Results & Conclusion** - So sánh mô hình, kết luận tối ưu

### ✅ Markdown Headers:

```markdown
# Problem Name

## 1. Define Problem

### 1.1 Problem Description

## 2. Prepare Problem

### 2.1 Load Libraries

### 2.2 Load Dataset

## 3. EDA

...
```

---

## 2️⃣ TIÊU CHUẨN CODE (CODE STANDARD)

### ✅ Đặt Tên Biến:

- [ ] DataFrames: `df_dataset`, `df_train`, `df_test`
- [ ] Arrays: `X`, `y` (hoặc `X_train`, `y_train`)
- [ ] Models: `model_dt`, `model_svm`, `model_knn` (với tên viết tắt thuật toán)
- [ ] Scalers/Encoders: `standard_scaler`, `minmax_scaler`, `label_encoder`
- [ ] Paths: `data_path`, `save_dir`, `exps_dir`
- [ ] Parameters: `params` dict để quản lý tất cả hyperparameters
- [ ] Avoid: `X1, X2, temp, var1, a, b` (tên quá chung chung)

### ✅ Comment & Documentation:

```python
# Load libraries
import numpy as np
import pandas as pd
# ... (một dòng cho mỗi import group)

# Set parameters
params = {
    "random_state": 42,
    "test_size": 0.3,
    "k_fold": 5
}

# Fix random seed for reproducibility
random.seed(params["random_state"])
np.random.seed(params["random_state"])
os.environ['PYTHONHASHSEED'] = str(params["random_state"])
```

### ✅ Các Thư Viện Ưu Tiên:

| Mục Đích        | Thư Viện                             | Priority |
| --------------- | ------------------------------------ | -------- |
| Data Processing | pandas, numpy                        | **MUST** |
| Visualization   | matplotlib, seaborn                  | **MUST** |
| ML Models       | scikit-learn                         | **MUST** |
| Metrics         | sklearn.metrics                      | **MUST** |
| Preprocessing   | sklearn.preprocessing                | **MUST** |
| Model Selection | sklearn.model_selection              | **MUST** |
| Advanced        | TensorFlow/PyTorch (Neural Networks) | OPTIONAL |

### ✅ Imports Format (Exact Order):

```python
# 1. System & Path
import os, sys

# 2. Visualization
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# 3. Data Processing
import numpy as np
import pandas as pd

# 4. ML & Metrics
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# 5. Utils
import joblib
import warnings
warnings.filterwarnings("ignore")

%matplotlib inline
```

---

## 3️⃣ QUY TẮC TIỀN XỬ LÝ (PREPROCESSING RULES)

### ✅ Missing Values (Dữ Liệu Thiếu):

- [ ] **Check:** `df.isnull().sum()` trước khi xử lý
- [ ] **Handle:**
  - Nếu < 5%: xóa hàng (`df.dropna()`)
  - Nếu 5-20%: fill bằng mean/median theo column
  - Nếu > 20%: drop cả column
  - Code: `df[col].fillna(df[col].mean(), inplace=True)`

### ✅ Outliers (Giá Trị Ngoại Lệ):

- [ ] **Detection:** IQR method
  ```python
  Q1, Q3 = df[col].quantile([0.25, 0.75])
  IQR = Q3 - Q1
  outliers = (df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)
  ```
- [ ] **Handle:** `df = df[~outliers]` (xóa outliers)

### ✅ Duplicate Data (Dữ Liệu Trùng):

- [ ] **Check:** `df.duplicated().sum()`
- [ ] **Remove:** `df.drop_duplicates(inplace=True)`

### ✅ Scaling (Chuẩn Hóa):

- [ ] **StandardScaler:** Dùng khi dữ liệu có phân bố **Gaussian** (Bell curve)
  ```python
  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X_train)
  ```
- [ ] **MinMaxScaler:** Dùng khi cần **giá trị trong range [0,1]**
  ```python
  from sklearn.preprocessing import MinMaxScaler
  scaler = MinMaxScaler()
  X_scaled = scaler.fit_transform(X_train)
  ```
- [ ] **RULE:** Fit trên train, transform train & test (tránh data leakage)

### ✅ Encoding (Mã Hóa):

- [ ] **LabelEncoder:** Cho biến categorical với order (True/False, Low/Medium/High)
  ```python
  le = LabelEncoder()
  df['class'] = le.fit_transform(df['class'])
  ```
- [ ] **OneHotEncoder:** Cho biến categorical không có order (màu, loài)
  ```python
  from sklearn.preprocessing import OneHotEncoder
  X_encoded = pd.get_dummies(df, columns=['category'])
  ```

### ✅ Train/Test Split:

- [ ] **Default ratio:** 70/30 (train/test)
  ```python
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.3, random_state=42
  )
  ```
- [ ] **RULE:** Luôn **cố định random_state** để reproducibility

---

## 4️⃣ TIÊU CHUẨN VISUALIZATION (VISUALIZATION STANDARD)

### ✅ Biểu Đồ Bắt Buộc Cho Mỗi Dataset:

| Thứ Tự | Loại Biểu Đồ            | Mục Đích                    | Code Template                                 |
| ------ | ----------------------- | --------------------------- | --------------------------------------------- |
| 1      | **Thongtin chung**      | Hiển thị shape, types, head | `display.display(df.head(5))`                 |
| 2      | **Distribution Plot**   | Xem phân bố từng feature    | `plt.hist(df[col])` hoặc `sns.histplot()`     |
| 3      | **Box Plot**            | Phát hiện outliers          | `sns.boxplot(data=df)`                        |
| 4      | **Correlation Heatmap** | Mối liên hệ giữa features   | `sns.heatmap(df.corr(), annot=True)`          |
| 5      | **Pair Plot**           | So sánh features vs target  | `sns.pairplot(df, hue='class')`               |
| 6      | **Class Distribution**  | Cân bằng dữ liệu            | `df['class'].value_counts().plot(kind='bar')` |
| 7      | **Confusion Matrix**    | Đánh giá mô hình            | `ConfusionMatrixDisplay(cm).plot()`           |

### ✅ Cấu Trúc Plot Standard:

```python
# EDA Plot (nhỏ)
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, i)
# ... plot code
plt.title("Title", fontsize=12, fontweight='bold')
plt.xlabel("X Label"); plt.ylabel("Y Label")
plt.tight_layout()
plt.show()

# Heatmap (lớn)
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Matrix", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### ✅ Colormap & Định Dạng:

- [ ] **Heatmap:** `cmap='coolwarm'` hoặc `cmap='RdBu_r'`
- [ ] **Distribution:** `color='skyblue'` hoặc `color='steelblue'`
- [ ] **Bar Chart:** `color='coral'` hoặc default palette
- [ ] **Figure Size:**
  - Single plot: `(10, 6)`
  - Multiple subplots: `(12, 8)` hoặc `(15, 10)`
  - Heatmap: `(12, 8)` trở lên

### ✅ Labels & Titles:

- [ ] **Title:** Bold, font size 12-14, mô tả rõ
- [ ] **X/Y Labels:** Rõ ràng, có unit nếu cần (cm, kg, $, ...)
- [ ] **Annotation:** Hiển thị con số trực tiếp trên biểu đồ

---

## 5️⃣ PHONG CÁCH LẬP LUẬN (REASONING STYLE)

### ✅ Nhận Xét Sau Mỗi Biểu Đồ:

**Format: [Hiện tượng]: [Con số] => [Ý nghĩa thực tế]**

#### ❌ SAI (Quá ngắn, không có ý nghĩa):

```
Correlation matrix: X có tương quan với Y
```

#### ❌ SAI (Quá dài, lặp lại):

```
Từ biểu đồ box plot, chúng ta có thể thấy rằng sepal-length
có khá nhiều giá trị nằm ngoài phạm vi thông thường do...
```

#### ✅ ĐÚNG (Súc tích + Con số + Ý nghĩa):

```
**Sepal-length correlation:** Setosa có tương quan mạnh
(r=0.82) với petal-length => những cánh hoa dài hơn
là dấu hiệu nhận biết Setosa.

**Distribution:** 73% outliers ở hàng 35 => loại bỏ 1 record.

**Class balance:** Mỗi loài có 50 mẫu (33.3%) => data cân bằng tốt.
```

### ✅ Cấu Trúc Nhận Xét:

- [ ] **Hiện tượng quan sát:** (con số cụ thể)
- [ ] **Hành động:** (quyết định tiền xử lý)
- [ ] **Lý do:** (tại sao thực tế)

### ✅ Độ Chi Tiết Theo Context:

| Context           | Style                     | Example                                                                                                                     |
| ----------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **EDA Phase**     | **Chi tiết + Giải thích** | Gia Dụng: "Sepal-width của Versicolor trung bình nhỏ hơn Virginica 0.3cm (2.77 vs 3.15), nên feature này tốt để phân biệt." |
| **Preprocessing** | **Súc tích + Con số**     | "Xóa 3 outliers (4.3% train set), giữ 145 mẫu."                                                                             |
| **Modeling**      | **Thống kê**              | "SVM: 96% accuracy với kernel='rbf'. DecisionTree: 98% nhưng có overfitting (train: 100%)."                                 |
| **Conclusion**    | **Ngắn gọn**              | "Chọn SVM vì cân bằng tốt giữa accuracy & generalization."                                                                  |

---

## 6️⃣ CẤU TRÚC TÌM THAM SỐ TỐI ƯU (HYPERPARAMETER TUNING)

### ✅ GridSearchCV (Tuần Tự Từng Tham Số):

```python
from sklearn.model_selection import GridSearchCV

# Step 1: Define parameter grid
param_grid = {
    'max_depth': [5, 10, 15, 20],
    'min_samples_split': [2, 5, 10],
    'criterion': ['gini', 'entropy']
}

# Step 2: Create GridSearch
model = DecisionTreeClassifier(random_state=42)
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,  # 5-Fold Cross-validation
    scoring='accuracy',
    n_jobs=-1  # Use all processors
)

# Step 3: Fit & Get results
grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.4f}")

# Step 4: Evaluate on test set
y_pred = grid_search.predict(X_test)
print(f"Test accuracy: {accuracy_score(y_test, y_pred):.4f}")
```

### ✅ K-Fold Cross-Validation (Đánh Giá Ổn Định):

```python
from sklearn.model_selection import KFold, cross_val_score

# Define K-Fold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Evaluate model
model = SVC(kernel='rbf')
scores = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')

print(f"Fold scores: {scores}")
print(f"Mean accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

### ✅ Hold-Out Validation (Training Split):

```python
X_train_sub, X_val, y_train_sub, y_val = train_test_split(
    X_train, y_train, test_size=0.3, random_state=42
)

model.fit(X_train_sub, y_train_sub)
val_score = accuracy_score(y_val, model.predict(X_val))
```

### ✅ So Sánh Mô Hình:

```python
models = {
    'Decision Tree': DecisionTreeClassifier(max_depth=15),
    'SVM': SVC(kernel='rbf', C=1.0),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5)
    results[name] = scores.mean()
    print(f"{name}: {scores.mean():.4f} +/- {scores.std():.4f}")
```

### ✅ Visualization So Sánh:

```python
# Plot model comparison
model_names = list(results.keys())
accuracies = list(results.values())

plt.figure(figsize=(10, 6))
plt.bar(model_names, accuracies, color=['coral', 'steelblue', 'lightgreen'])
plt.ylabel('Accuracy'); plt.xlabel('Model')
plt.title('Model Comparison')
plt.ylim([0.8, 1.0])
plt.xticks(rotation=15)
for i, v in enumerate(accuracies):
    plt.text(i, v + 0.01, f'{v:.3f}', ha='center', fontweight='bold')
plt.tight_layout(); plt.show()
```

### ✅ Parameters Dict Template:

```python
params = {
    "random_state": 42,
    "test_size": 0.3,
    "k_fold": 5,

    # Decision Tree
    "dt_max_depth": [10, 15, 20],
    "dt_min_samples_split": [2, 5],

    # SVM
    "svm_kernel": ['linear', 'rbf'],
    "svm_C": [0.1, 1, 10],

    # KNN
    "knn_k": [3, 5, 7, 9],

    # GridSearch
    "cv_fold": 5
}
```

---

## 📊 CHECKLIST HOÀN THIỆN MỖI DỰ ÁN

- [ ] Define Problem rõ ràng (input, output, type)
- [ ] Load libraries đúng thứ tự
- [ ] Check missing values & outliers
- [ ] EDA có đủ 7 loại biểu đồ
- [ ] Preprocessing có nhận xét giải thích
- [ ] Train/Test split với random_state cố định
- [ ] Xây dựng >= 3 mô hình khác nhau
- [ ] K-Fold Cross-validation (k=5)
- [ ] GridSearch hoặc parameter tuning
- [ ] Confusion Matrix cho mỗi mô hình
- [ ] So sánh mô hình với visualization
- [ ] Conclusion rõ ràng (mô hình tốt nhất = ?)
- [ ] Code comments đầy đủ
- [ ] Biến có tên rõ ràng (không X1, Y1, temp)
- [ ] Tất cả random seed = 42 (để reproduce)

---

## 🎯 SUMMARY

| Yếu Tố            | Quy Tắc                                                                         |
| ----------------- | ------------------------------------------------------------------------------- |
| **Struktur**      | Define → Prepare → EDA → Preprocess → Split → Model → Eval → Tune → Conclude    |
| **Code**          | Tên biến rõ, `params` dict, imports ordered, random_state=42                    |
| **Preprocessing** | Check null/dup, remove outliers (IQR), scale (Standard/MinMax), encode (LE/OHE) |
| **Visualization** | 7 plot bắt buộc, figsize (10,6), cmap coolwarm, titles bold                     |
| **Nhận xét**      | [Hiện tượng]: [Con số] => [Ý nghĩa thực tế]                                     |
| **Tuning**        | GridSearchCV(cv=5) + K-Fold + So sánh Bar Chart                                 |

---

**Created:** 2026-03-25  
**Version:** 1.0  
**Based on:** lab07_ml_models (iris_classification + MinhHoa1 + sample_project)
