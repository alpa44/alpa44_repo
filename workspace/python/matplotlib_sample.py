import matplotlib as mpl
import matplotlib.pylab as plt

##########################################
# line plot
#########################################

# x축 생략시 x축은 0, 1, 2, 3이 됨
#plt.plot([1, 4, 9, 16])
#plt.show()


# x축과 y축 지정
#plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
#plt.show()

# 스타일지정
# 색깔, 마커, 선 순서로 지정함
# 색깔 : blue(b), green(g), red(r), cyan(c), magenta(m), yellow(y), block(k), white(w)
# 마커 : point(.), pixel(,), circle(o), triangle_down(v), triangle_up(^),
#        triangle_left(<), triangle_right(>), tri_down(1), tri_up(2), tri_left(3),
#        tri_right(4), square(s), pentagon(p), star(*), hexagon1(h),
#        hexagon2(H), plus(+), x marker(x), diamond(D), thin_diamond(d)
# 선 : solid line(-), dashed line(--), dash-dot line(-.), dotted(:)
#plt.plot([1,4,9,16], 'bs:')
#plt.show()


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
#plt.plot([1,4,9,16], c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5,
#        mfc="r")
#plt.show()


# 그림 범위지정
# xlim, ylim에서 최소, 최대값 지정
plt.plot([1,4,9,16], c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5,
        mfc="r")
plt.xlim(-10, 10)
plt.ylim(-10, 30)
plt.show()
