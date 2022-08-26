#include<iostream>
#include<Windows.h>
#include<tchar.h>
#include<DirectXMath.h>
#include<DirectXPackedVector.h>

using namespace std;
using namespace DirectX;
using namespace DirectX::PackedVector;

ostream &XM_CALLCONV operator<<(ostream &os, FXMVECTOR v) {
	XMFLOAT3 dest;
	XMStoreFloat3(&dest, v);

	cout << "(" << dest.x << "," << dest.y << "," << dest.z << ")";
	return os;
}

int main() {
	cout.setf(ios_base::boolalpha);

	if (!XMVerifyCPUSupport()) {
		cout << "directx is fail !!\n";
		return 0;
	}

	XMVECTOR n = XMVectorSet(1.0f, 0.0f, 0.0f, 0.0f);
	XMVECTOR u = XMVectorSet(1.0f, 2.0f, 3.0f, 0.0f);
	XMVECTOR v = XMVectorSet(-2.0f, 1.0f, -3.0f, 0.0f);
	XMVECTOR w = XMVectorSet(0.707f, 0.707f, 0.0f, 0.0f);

	// 向量加法：利用XMVECTOR类型的加法运算符+
	XMVECTOR a = u + v;

	// 向量减法：利用XMVECTOR类型的减法运算符- 
	XMVECTOR b = u - v;

	// 标量乘法：利用XMVECTOR类型的标量乘法运算符*
	XMVECTOR c = 10.0f * u;

	// ||u||
	XMVECTOR L = XMVector3Length(u);

	// d = u / ||u||
	XMVECTOR d = XMVector3Normalize(u);

	// s = u dot v
	XMVECTOR s = XMVector3Dot(u, v);

	// e = u x v 
	XMVECTOR e = XMVector3Cross(u, v);

	// 求出proj_n(w)和perp_n(w)
	XMVECTOR projW;
	XMVECTOR perpW;
	XMVector3ComponentsFromNormal(&projW, &perpW, w, n);

	// projW + perpW == w?
	bool equal = XMVector3Equal(projW + perpW, w) != 0;
	bool notEqual = XMVector3NotEqual(projW + perpW, w) != 0;

	// projW与perpW之间的夹角应为90度
	XMVECTOR angleVec = XMVector3AngleBetweenVectors(projW, perpW);
	float angleRadians = XMVectorGetX(angleVec);
	float angleDegrees = XMConvertToDegrees(angleRadians);

	cout << "u             = " << u << endl;
	cout << "v             = " << v << endl;
	cout << "w             = " << w << endl;
	cout << "n             = " << n << endl;
	cout << "a = u + v     = " << a << endl;
	cout << "b = u - v     = " << b << endl;
	cout << "c = 10 * u    = " << c << endl;
	cout << "d = u / ||u|| = " << d << endl;
	cout << "e = u x v     = " << e << endl;
	cout << "L = ||u||     = " << L << endl;
	cout << "s = u.v       = " << s << endl;
	cout << "projW         = " << projW << endl;
	cout << "perpW         = " << perpW << endl;
	cout << "projW + perpW == w = " << equal << endl;
	cout << "projW + perpW != w = " << notEqual << endl;
	cout << "angle         = " << angleDegrees << endl;

	return 0;
}


/*由于在计算机内无法完全等于，只能无限接近，过(float)1^100 并非为 (int)1*/


