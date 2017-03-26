import numpy as np
import matplotlib.pyplot as plt

##########################################
# line plot
#########################################

# x축 생략시 x축은 0, 1, 2, 3이 됨
"""
plt.plot([1, 4, 9, 16])
plt.show()
"""


# x축과 y축 지정
"""
plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
plt.show()
"""

# 스타일지정
# 색깔, 마커, 선 순서로 지정함
# 색깔 : blue(b), green(g), red(r), cyan(c), magenta(m), yellow(y), block(k), white(w)
# 마커 : point(.), pixel(,), circle(o), triangle_down(v), triangle_up(^),
#        triangle_left(<), triangle_right(>), tri_down(1), tri_up(2), tri_left(3),
#        tri_right(4), square(s), pentagon(p), star(*), hexagon1(h),
#        hexagon2(H), plus(+), x marker(x), diamond(D), thin_diamond(d)
# 선 : solid line(-), dashed line(--), dash-dot line(-.), dotted(:)
"""
plt.plot([1,4,9,16], 'bs:')
plt.show()
"""


# 기타스타일
# http://matplotlib.org/1.5.1/api/lines_api.html#matplotlib.lines.Line2D 참고
# color(c) : 선색깔
# linewidth(lw) : 선굵기
# linestyle(ls) : 선스타일
# marker : 마커종류
# markersize(ms) : 마커크기
# markeredgecolor(mec) : 마커 선 색깔
# markeredgewidth(mew) : 마커 선 굵기
# markerfacecolor(mfc) : 마커 내부 색깔
"""
plt.plot([1,4,9,16], c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5,
        mfc="r")
plt.show()
"""


# 그림 범위지정
# xlim, ylim에서 최소, 최대값 지정
"""
plt.plot([1,4,9,16], c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5,
        mfc="r")
plt.xlim(-10, 10)
plt.ylim(-10, 30)
plt.show()
"""

# 틱 설정
# 틱 : 플롯이나 차트에서 축상의 위치 표시 지점
# 틱라벨 : 틱 위에 써진 숫자 혹은 글자
# xticks, yticks로 틱라벨 지정
# 틱 라벨 문자열에는 $$사이에 LaTeX 수학 문자식 넣을수 있다
"""
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, +1])
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$',
'0', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1], ["Low", "Zero", "High"])
plt.grid(False) # grid없애기
plt.show()
"""


# 여러개 선 그리기
# x, y, 스타일을 여러개 지정하면 됨
"""
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, 0.5*t**2, 'bs:', t, 0.2*t**3, 'g^-')
plt.show()
"""


# 하나의 그림에 복수의 plot명령 적용 : 홀드
# hold(True) : 겹치기 시작
# hold(False) : 겹치기 종료
"""
plt.plot([1,4,9,16], c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5,
        mfc="r")
plt.hold(True)
plt.plot([9,16,4,1], c="k", lw=3, ls=":", marker="s", ms=10, mec="m", mew=5,
        mfc="c")
plt.hold(False)
plt.show()
"""


# 범례
# legent명령으로 범례 추가
# loc인수로 범례의 위치 지정
# loc : best(0), upper right(1), upper left(2), lower left(3),
#       lower right(4), right(5), center left(6), center right(7)
#       lower center(8), upper center(9), center(10)
"""
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, label="cosine")
plt.hold(True)
plt.plot(X, S, label="sine")
plt.legend(loc=5)
plt.show()
"""

# x축, y축 라벨, 타이틀
# xlabel, ylabel, title로 지정
"""
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, label="cosine")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Cosine Plot")
plt.show()
"""

# 부가설명
# annotate명령을 사용하여 그림내에 화살표를 포함한 부가 설명 넣을수 있음
"""
X = np.linspace(-np.pi, np.pi, 256)
S = np.sin(X)
plt.plot(X, S, label="sine")
plt.scatter([0], [0], color="r", linewidth=10)
plt.annotate(r'$(0,0)$', xy=(0, 0), xycoords='data', xytext=(-50, 50),
            textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", linewidth=3, color="g"))
plt.show()
"""


# Figure [ Axes [ Axis] ] 의 구조이다
# Figure : 여러개의 윈도우를 띄우거나, 그림의 크기 지정시 사용
#          plot사용시 자동으로 Figure를 생성하므로 명시적으로 생성할 필요는
#          없음
# figure객체를 얻으려면 gcf 명령 사용
"""
f1 = plt.figure(figsize=(100,2))
plt.plot(np.random.randn(100))
plt.show()
"""
"""
f1 = plt.figure(1)
plt.plot([1,2,3,4], 'ro:')
f2= plt.gcf()
print(f1, id(f1))
print(f2, id(f2))
plt.show()
"""


# Axes와 Subplot
# 하나의 윈도우(Figure)안에 여러개의 플롯을 배열하는 경우 각각의 플롯은
# Axes라고 불리는 객체에 속함
# subplot 명령으로 Axes객체를 생성, plot명령 사용시 자동으로 Axes를 생성함
# subplot은 그리드 형태의 Axes객체들을 생성
# Figure가 행렬(matrix)이고 Axes가 행렬의 원소라고 생각하면 됨.
# 위와 아래 두개의 플롯이 있는 경우 2X1행렬
# subplot은 3개의 인수를 가지고 처음 2개가 행렬 정의, 세번째가 위치 지정
"""
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

ax1 = plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('A tale of 2 subplots')
plt.ylabel('Dampled oscillation')
print(ax1)

ax2 = plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
print(ax2)

plt.show()
"""

# subplot의 인수는 (2,2,1)를 줄여서 221로 표시 가능
"""
plt.subplot(221); plt.plot([1,2]); plt.title(1)
plt.subplot(222); plt.plot([1,2]); plt.title(2)
plt.subplot(223); plt.plot([1,2]); plt.title(3)
plt.subplot(224); plt.plot([1,2]); plt.title(4)
plt.tight_layout()
plt.show()
"""


# xkcd 스타일
X = np.linspace(-3, 3, 4096)
C = np.cos(X)

with plt.xkcd():
    plt.title('XKCD style plot!!!')
    plt.plot(X, C, label="cosine")
    t = 2 * np.pi / 3
    plt.scatter(t, np.cos(t), 50, color='blue')
    plt.annotate(r'0.5 Here', xy=(t, np.cos(t)), xycoords='data', xytext=(-90,
        -50), textcoords='offset points', fontsize=16,
        arrowprops=dict(arrowstyle="->", linewidth=3, color="g"))
plt.show()


