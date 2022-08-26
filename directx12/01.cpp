/*原来高数这么重要，焯！！！*/

#include<Windows.h>
#include<tchar.h>
#include<DirectXMath.h>//使用directxmath库
#include<DirectXPackedVector.h>//使用一些相关的数据类型
#include<xmmintrin.h>//__m128 定义

using namespace DirectX;
//using namespace DirectX::PackedVector;

//DitectXMath 的相关代码位于 DirectX命名空间中
//DirectXPackedVector 的相关代码位于DirectX::PackedVector 的命名空间中

typedef __m128 XMVECTOR;//XMVECTOR 为directx的核心向量，将被映射到SIMD寄存器(128位)上
                        //一次处理4个32位的浮点数，为核心计算技术

// 以下为定义
/*
struct XMFLOAT2 { //2D向量定义如下
    float x;
    float y;

    XMFLOAT2() { }

    XMFLOAT2(float _x, float _y):x(_x),y(_y) { }

    explicit XMFLOAT2(_In_reads_(2) const float* pArray) :x(pArray[0]), y(pArray[1]) { }
    //explicit 只能用于修饰只有一个参数的类构造函数

    XMFLOAT2& operator= (const XMFLOAT2& Float2)
    {
        x = Float2.x; y = Float2.y; return *this;
    }
};

struct XMFLOAT3 { //3D向量定义如下
    float x;
    float y;
    float z;

    XMFLOAT3() { }

    XMFLOAT3(float _x, float _y, float _z) :x(_x), y(_y), z(_z) { }

    explicit XMFLOAT3(_In_reads_(3) const float* pArray) :
        x(pArray[0]), y(pArray[1]), z(pArray[2]) { }

    XMFLOAT3& operator= (const XMFLOAT3& Float3)
    {
        x = Float3.x; y = Float3.y, z = Float3.z; return *this;
    }
};

struct XMFLOAT4 { //4D向量定义如下
    float x;
    float y;
    float z;
    float w;

    XMFLOAT4() { }

    XMFLOAT4(float _x, float _y, float _z,float _w) :x(_x), y(_y), z(_z), w(_w) { }

    explicit XMFLOAT4(_In_reads_(4) const float* pArray) :
        x(pArray[0]), y(pArray[1]), z(pArray[2]), w(pArray[3]) { }

    XMFLOAT4& operator= (const XMFLOAT4& Float4)
    {
        x = Float4.x; y = Float4.y, z = Float4.z,w = Float4.w ; return *this;
    }
};
*/
//将上述转换为XMVECTOR类型才能更好的发挥处SIMD的技术

/* 以下为转变过程方法*/
// 从 XMFloatN 加载到 XMVECTOR
XMVECTOR XM_CALLCONV XMLoadFloat2(const XMFLOAT2* pSource);
XMVECTOR XM_CALLCONV XMLoadFloat3(const XMFLOAT3* pSource);
XMVECTOR XM_CALLCONV XMLoadFloat4(const XMFLOAT4* pSource);

// 将 XMVECTOR 存储到 XMFloatN
void XM_CALLCONV XMStoreFLoat2(XMFLOAT2* pDestination, XMVECTOR V);
void XM_CALLCONV XMStoreFLoat3(XMFLOAT3* pDestination, XMVECTOR V);
void XM_CALLCONV XMStoreFLoat4(XMFLOAT4* pDestination, XMVECTOR V);

// 从 XMVECTOR 获取单个分量
float XM_CALLCONV XMVectorGetX(XMVECTOR V);
float XM_CALLCONV XMVectorGetY(XMVECTOR V);
float XM_CALLCONV XMVectorGetZ(XMVECTOR V);
float XM_CALLCONV XMVectorGetW(XMVECTOR V);

// 将 单个分量 存储到 XMVECTOR
XMVECTOR XM_CALLCONV XMVectorSetX(XMVECTOR V, float x);
XMVECTOR XM_CALLCONV XMVectorSetY(XMVECTOR V, float y);
XMVECTOR XM_CALLCONV XMVectorSetZ(XMVECTOR V, float z);
XMVECTOR XM_CALLCONV XMVectorSetW(XMVECTOR V, float w);

/*受不同平台的影响，将用 FXMVECTOR,GXMVECTOR,HXMVECTOR,CXMVECTOR 类型来传递XMVECTOR的参数
* 规则如下：
* 1.前三个 XMVECTOR 应当使用 FXMVECTOR类型
* 2.第四个 XMVECTOR 应当使用 GXMVECTOR类型
* 3.第5，6个 XMVECTOR 应当使用 HXMVECTOR类型
* 4.其余的使用 CXMVECTOR类型
*/

/*
XMVECTOR 的常向量实例应用 XMVECTORF32 类型来表示,16字节对齐吗，
*/

//例：
static const XMVECTORF32 g_vHalfVetcor = { 0.5f,0.5f,0.5f,0.5f };
static const XMVECTORF32 g_vZero = { 0.0f,0.0f,0.0f,0.0f };

/*数学库中还提供了其转换至XMVETCOR类型的运算符,定义如下：*/
/*
_declspec(align(16)) struct XMVECTORF32 {
    union {
        float f[4];
        XMVECTCOR v;
    };

    inline operator XMVECTOR() const { return v; }
    inline operator const float* () { return f; }
#if !defined(_XM_NO_INTRINSICS_) && defined(_XM_SSE_INTRINSICS)
    inline operator _m128i() const { return _mm_castps_si128(v); }
    inline operator _m128d() const { return _mm_castps_pd(v); }
#endif

};
*/

/*与高中数学中向量相似*/

const float XM_PI = 3.141592654f;
const float XM_2PI = 6.28;
/*且有用到弧度制转换*/


/*设置XMVECTOR的类型*/

//返回0
XMVECTOR XM_CALLCONV XMVectorZere();

//返回（1，1，1，1）
XMVECTOR XM_CALLCONV XMVectorSplatOne();

//返回 (x,y,z,w)
XMVECTOR XM_CALLCONV XMVectorSet(float x, float y, float z, float w);

//返回向量（value,value,...）
XMVECTOR XM_CALLCONV XMVectorZere();

//返回向量(Vx,Vx,Vx,Vx)
XMVECTOR XM_CALLCONV XMVectorSplatX(FXMVECTOR v);

//返回向量(Vy,Vy,Vy,Vy)
XMVECTOR XM_CALLCONV XMVectorSplatY(FXMVECTOR v);
