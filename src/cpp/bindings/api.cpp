#include "pybind11/pybind11.h"
#include "pybind11/stl.h"
#include "cpp/bindings/ParamSetProxy.h"
#include "core/api.h"

namespace py = pybind11;

using std::vector;
using std::string;
using std::cout;

void Init(int nThreads,
          bool quick,
          bool quiet,
          bool verbose) {
  Options options;
  options.nThreads = nThreads;
  options.quickRender = quick;
  options.quiet = quiet;
  options.verbose = verbose;

  printf("pbrt version 3 [Detected %d cores]\n",
         NumSystemCores());
  printf("Copyright (c)1998-2015 Matt Pharr, Greg Humphreys, and Wenzel Jakob.\n");
  printf("The source code to pbrt (but *not* the book contents) is covered by the BSD License.\n");
  printf("See the file LICENSE.txt for the conditions of the license.\n");
  fflush(stdout);

  pbrtInit(options);
}

void FlushSTDOUT() {
  fflush(stdout);
}

void ConcatTransform(vector<Float> transform) {
  if (transform.size() != 16) {
    Error("Expected a list of size 16");
  };
  pbrtConcatTransform(transform.data());
}

void Transform(vector<Float> transform) {
  if (transform.size() != 16) {
    Error("Expected a list of size 16");
  };
  pbrtTransform(transform.data());
}

void PixelFilter(const string& name, const ParamSetProxy& proxy) {
  pbrtPixelFilter(name, proxy.getParamSet());
}

void Film(const string& type, const ParamSetProxy& proxy) {
  pbrtFilm(type, proxy.getParamSet());
}

void Sampler(const string& name, const ParamSetProxy& proxy) {
  pbrtSampler(name, proxy.getParamSet());
}

void Accelerator(const string& name, const ParamSetProxy& proxy) {
  pbrtAccelerator(name, proxy.getParamSet());
}

void Integrator(const string& name, const ParamSetProxy& proxy) {
  pbrtIntegrator(name, proxy.getParamSet());
}

void Camera(const string& name, const ParamSetProxy& proxy) {
  pbrtCamera(name, proxy.getParamSet());
}

void MakeNamedMedium(const string& name, const ParamSetProxy& proxy) {
  pbrtMakeNamedMedium(name, proxy.getParamSet());
}

void Texture(const string& name, const string& type, const string& texname, const ParamSetProxy& proxy) {
  pbrtTexture(name, type, texname, proxy.getParamSet());
}

void Material(const string& name, const ParamSetProxy& proxy) {
  pbrtMaterial(name, proxy.getParamSet());
}

void MakeNamedMaterial(const string& name, const ParamSetProxy& proxy) {
  pbrtMakeNamedMaterial(name, proxy.getParamSet());
}

void LightSource(const string& name, const ParamSetProxy& proxy) {
  pbrtLightSource(name, proxy.getParamSet());
}

void AreaLightSource(const string& name, const ParamSetProxy& proxy) {
  pbrtAreaLightSource(name, proxy.getParamSet());
}

void Shape(const string& name, const ParamSetProxy& proxy) {
  pbrtShape(name, proxy.getParamSet());
}

PYBIND11_PLUGIN(pbrt) {
  py::module m("pbrt", "PBRT bindings");

  py::class_<ParamSetProxy>(m, "ParamSet")
      .def(py::init())
      .def("AddFloat", &ParamSetProxy::AddFloat)
      .def("AddInt", &ParamSetProxy::AddInt)
      .def("AddBool", &ParamSetProxy::AddBool)
      .def("AddPoint2f", &ParamSetProxy::AddPoint2f, "Input: float array x1 y1, x2 y2 ...")
      .def("AddVector2f", &ParamSetProxy::AddVector2f, "Input: float array x1 y1, x2 y2 ...")
      .def("AddPoint3f", &ParamSetProxy::AddPoint3f, "Input: float array x1 y1 z1, x2 y2 z2 ...")
      .def("AddVector3f", &ParamSetProxy::AddVector3f, "Input: float array x1 y1 z1, x2 y2 z2 ...")
      .def("AddNormal3f", &ParamSetProxy::AddNormal3f, "Input: float array x1 y1 z1, x2 y2 z2 ...")
      .def("AddRGBSpectrum", &ParamSetProxy::AddRGBSpectrum, "Input: float array r1 g1 b1 r2 g2 b2 ...")
      .def("AddString", &ParamSetProxy::AddString)
      .def("AddTexture", &ParamSetProxy::AddTexture);

  m.def("Init", &Init,
        py::arg("nThreads") = 0,
        py::arg("quickRender") = false,
        py::arg("quiet") = false,
        py::arg("verbose") = false);

  m.def("Cleanup", &pbrtCleanup);
  m.def("Identity", &pbrtIdentity);
  m.def("Translate", &pbrtTranslate);
  m.def("Rotate", &pbrtRotate);
  m.def("Scale", &pbrtScale);
  m.def("LookAt", &pbrtLookAt);
  m.def("ConcatTransform", &ConcatTransform);
  m.def("Transform", &Transform);
  m.def("CoordinateSystem", &pbrtCoordinateSystem);
  m.def("CoordSysTransform", &pbrtCoordSysTransform);
  m.def("ActiveTransformAll", &pbrtActiveTransformAll);
  m.def("ActiveTransformEndTime", &pbrtActiveTransformEndTime);
  m.def("ActiveTransformStartTime", &pbrtActiveTransformStartTime);
  m.def("TransformTimes", &pbrtTransformTimes);
  m.def("PixelFilter", &PixelFilter);
  m.def("Film", &Film);
  m.def("Sampler", &Sampler);
  m.def("Accelerator", &Accelerator);
  m.def("Integrator", &Integrator);
  m.def("Camera", &Camera);
  m.def("MakeNamedMedium", &MakeNamedMedium);
  m.def("MediumInterface", &pbrtMediumInterface);

  m.def("WorldBegin", &pbrtWorldBegin);

  m.def("AttributeBegin", &pbrtAttributeBegin);
  m.def("AttributeEnd", &pbrtAttributeEnd);
  m.def("TransformBegin", &pbrtTransformEnd);
  m.def("Texture", &Texture);
  m.def("Material", &Material);
  m.def("MakeNamedMaterial", &MakeNamedMaterial);
  m.def("NamedMaterial", &pbrtNamedMaterial);
  m.def("LightSource", &LightSource);
  m.def("AreaLightSource", &AreaLightSource);
  m.def("Shape", &Shape);
  m.def("ReverseOrientation", &pbrtReverseOrientation);
  m.def("ObjectBegin", &pbrtObjectBegin);
  m.def("ObjectEnd", &pbrtObjectEnd);
  m.def("ObjectInstance", &pbrtObjectInstance);

  m.def("WorldEnd", &pbrtWorldEnd);
  m.def("flush_STDOUT", &FlushSTDOUT);
  return m.ptr();
}
