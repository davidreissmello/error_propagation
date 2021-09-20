import math
from error_propagation import Sampler


@Sampler.make_math_sampler_compatible
def exp(x):
    return math.exp(x)


@Sampler.make_math_sampler_compatible
def expm1(x):
    return math.expm1(x)


@Sampler.make_math_sampler_compatible
def log(x):
    return math.log(x)


@Sampler.make_math_sampler_compatible
def log1p(x):
    return math.log1p(x)


@Sampler.make_math_sampler_compatible
def log2(x):
    return math.log2(x)


@Sampler.make_math_sampler_compatible
def log10(x):
    return math.log10(x)


@Sampler.make_math_sampler_compatible
def sqrt(x):
    return math.sqrt(x)


@Sampler.make_math_sampler_compatible
def acos(x):
    return math.acos(x)


@Sampler.make_math_sampler_compatible
def asin(x):
    return math.asin(x)


@Sampler.make_math_sampler_compatible
def atan(x):
    return math.atan(x)


@Sampler.make_math_sampler_compatible
def cos(x):
    return math.cos(x)


@Sampler.make_math_sampler_compatible
def sin(x):
    return math.sin(x)


@Sampler.make_math_sampler_compatible
def tan(x):
    return math.tan(x)


@Sampler.make_math_sampler_compatible
def degrees(x):
    return math.degrees(x)


@Sampler.make_math_sampler_compatible
def radians(x):
    return math.radians(x)


@Sampler.make_math_sampler_compatible
def cosh(x):
    return math.acosh(x)


@Sampler.make_math_sampler_compatible
def asinh(x):
    return math.asinh(x)


@Sampler.make_math_sampler_compatible
def atanh(x):
    return math.atanh(x)


@Sampler.make_math_sampler_compatible
def cosh(x):
    return math.cosh(x)


@Sampler.make_math_sampler_compatible
def sinh(x):
    return math.sinh(x)


@Sampler.make_math_sampler_compatible
def tanh(x):
    return math.tanh(x)


@Sampler.make_math_sampler_compatible
def erf(x):
    return math.erf(x)


@Sampler.make_math_sampler_compatible
def erfc(x):
    return math.erfc(x)


@Sampler.make_math_sampler_compatible
def gamma(x):
    return math.gamma(x)


@Sampler.make_math_sampler_compatible
def lgamma(x):
    return math.lgamma(x)
