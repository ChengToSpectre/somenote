#include<iostream>
#include<Windows.h>
#include<tchar.h>
#include<DirectXMath.h>
#include<DirectXPackedVector.h>
using namespace std;
using namespace DirectX;
using namespace DirectX::PackedVector;

ostream &XM_CALLCONV operator << (ostream& os, FXMVECTOR v) //重载<<输出符号
{
	XMFLOAT3 dest;
	XMStoreFloat3(&dest, v);

	os << "(" << dest.x << "," << dest.y << "," << dest.z << ")";
	return os;
}

int main() {
	cout.setf(ios_base::boolalpha);//bool类型以 true/false 输入/输出

	if (!XMVerifyCPUSupport())//检查Pentium4 AMD K8等后续版本的处理器 
	{
		cout << "directx math not supported!!!" << endl;
		return 0;
	}

	XMVECTOR p = XMVectorZero();
	XMVECTOR q = XMVectorSplatOne();
	XMVECTOR u = XMVectorSet(1.0f,2.0f,3.0f,4.0f);
	XMVECTOR v = XMVectorReplicate(-2.0f);
	XMVECTOR w = XMVectorSplatZ(u);

	cout << " p = " << p << endl;
	cout << " q = " << q << endl;
	cout << " u = " << u << endl;
	cout << " v = " << v << endl;
	cout << " w = " << w << endl;

	return 0;
}


/*向量函数， XM_CALLCONV 为加速指令 */

XMVECTOR XM_CALLCONV XMVector3Length(FXMVECTOR v);//返回v的长度
XMVECTOR XM_CALLCONV XMVector3LengthSq(FXMVECTOR v);//返回v的长度的绝对值
XMVECTOR XM_CALLCONV XMVector3Dot(FXMVECTOR v1,FXMVECTOR v2);//返回 v1*v2 的长度
XMVECTOR XM_CALLCONV XMVector3Cross(FXMVECTOR v1, FXMVECTOR v2);//返回 v1Xv2 的长度
XMVECTOR XM_CALLCONV XMVector3Normalize(FXMVECTOR v);//返回 v/(|v|) 即返回v方向的单位向量
XMVECTOR XM_CALLCONV XMVector3Orthogonal(FXMVECTOR v);//返回正交于 v 的一个向量
XMVECTOR XM_CALLCONV XMVector3AngleBetweenVectors(FXMVECTOR v1, FXMVECTOR v2);//返回 v1与v2 的夹角

void XM_CALLCONV XMVector3ComponentsFromNormal(
	XMVECTOR* pParallel,                         //返回proj(n)(v)
	XMVECTOR* pPerpendicular,                    //返回perp(n)(v)
	FXMVECTOR V,                                 //输入向量v
	FXMVECTOR Normal                             //输入规范化向量n
);

bool XM_CALLCONV XMVector3Equal(          //返回 v1 == v2？
	FXMVECTOR v1,                         //输入v1
	FXMVECTOR v2                          //输入v2
)



