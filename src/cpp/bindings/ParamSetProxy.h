#ifndef RENDERER_PARAMSETPROXY_H
#define RENDERER_PARAM

#include "core/paramset.h"

class ParamSetProxy {
 public:
  ParamSetProxy()
      : paramSet(new ParamSet) { }

  void AddFloat(const std::string &, std::vector<Float> values);
  void AddInt(const std::string &, std::vector<int> values);
  void AddBool(const std::string &, std::vector<bool> values);
  void AddPoint2f(const std::string &, std::vector<Float> values);
  void AddVector2f(const std::string &, std::vector<Float> values);
  void AddPoint3f(const std::string &, std::vector<Float> values);
  void AddVector3f(const std::string &, std::vector<Float> values);
  void AddNormal3f(const std::string &, std::vector<Float> values);
  void AddString(const std::string &, std::vector<std::string> values);
  void AddTexture(const std::string &, const std::string &);

  const ParamSet getParamSet() const;
 private:
  ParamSet *paramSet;
};

#endif //RENDERER_PARAMSETPROXY_H
