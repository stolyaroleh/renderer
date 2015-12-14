#include "cpp/bindings/ParamSetProxy.h"

template <typename T>
struct ArrayView {
  ArrayView(std::vector<T> values) {
    size = values.size();
    v = std::make_unique<T[]>(size);
    for (size_t i = 0; i < size; i++) {
      v[i] = values[i];
    }
  }
  std::unique_ptr<T[]> v;
  size_t size;
};

void ParamSetProxy::AddFloat(const std::string& name, std::vector<Float> values) {
  ArrayView<Float>* arrayView = new ArrayView<Float>(values);
  paramSet->AddFloat(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddInt(const std::string& name, std::vector<int> values) {
  ArrayView<int>* arrayView = new ArrayView<int>(values);
  paramSet->AddInt(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddBool(const std::string& name, std::vector<bool> values) {
  ArrayView<bool>* arrayView = new ArrayView<bool>(values);
  paramSet->AddBool(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddPoint2f(const std::string& name, std::vector<Float> values) {
  std::vector<Point2f> v;
  for (size_t i = 0; i < values.size() - 1; i+=2) {
    v.push_back(Point2f(values[i], values[i + 1]));
  }
  ArrayView<Point2f>* arrayView = new ArrayView<Point2f>(v);
  paramSet->AddPoint2f(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddVector2f(const std::string& name, std::vector<Float> values) {
  std::vector<Vector2f> v;
  for (size_t i = 0; i < values.size() - 1; i+=2) {
    v.push_back(Vector2f(values[i], values[i + 1]));
  }
  ArrayView<Vector2f>* arrayView = new ArrayView<Vector2f>(v);
  paramSet->AddVector2f(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddPoint3f(const std::string& name, std::vector<Float> values) {
  std::vector<Point3f> v;
  for (size_t i = 0; i < values.size() - 2; i+=3) {
    v.push_back(Point3f(values[i], values[i + 1], values[i + 2]));
  }
  ArrayView<Point3f>* arrayView = new ArrayView<Point3f>(v);
  paramSet->AddPoint3f(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddVector3f(const std::string& name, std::vector<Float> values) {
  std::vector<Vector3f> v;
  for (size_t i = 0; i < values.size() - 2; i+=3) {
    v.push_back(Vector3f(values[i], values[i + 1], values[i + 2]));
  }
  ArrayView<Vector3f>* arrayView = new ArrayView<Vector3f>(v);
  paramSet->AddVector3f(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddNormal3f(const std::string& name, std::vector<Float> values) {
  std::vector<Normal3f> v;
  for (size_t i = 0; i < values.size() - 2; i+=3) {
    v.push_back(Normal3f(values[i], values[i + 1], values[i + 2]));
  }
  ArrayView<Normal3f>* arrayView = new ArrayView<Normal3f>(v);
  paramSet->AddNormal3f(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddRGBSpectrum(const std::string& name, std::vector<Float> values) {
  ArrayView<Float>* arrayView = new ArrayView<Float>(values);
  paramSet->AddRGBSpectrum(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddString(const std::string& name, std::vector<std::string> values) {
  ArrayView<std::string>* arrayView = new ArrayView<std::string>(values);
  paramSet->AddString(name, std::move(arrayView->v), arrayView->size);
  delete arrayView;
}

void ParamSetProxy::AddTexture(const std::string& name, const std::string& texture) {
  paramSet->AddTexture(name, texture);
}

const ParamSet ParamSetProxy::getParamSet() const {
  return *paramSet;
}
