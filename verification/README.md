# 拉马努金45条公式验证模块

GNN预测的10条隐藏连接的数值验证代码。

## 7条高可信度连接验证

| # | 连接 | 脚本 | 验证方法 | 状态 |
|---|------|------|----------|------|
| 9 | q-超几何×Gamma | `v09_qhyper_gamma.py` | q→1极限数值 | ⚠️ 数学正确，数值溢出 |
| 2 | 秩矩×渐近 | `v02_rank_asymptotic.py` | 渐近比值 | ✅ 比值→1 |
| 8 | Theta×三次 | `v08_theta_cubic.py` | j不变量匹配 | ✅ j(i)=1728 |
| 6 | ζ(2n+1)×Beta | `v06_zeta_beta.py` | 50位精度积分 | ✅ 误差=0 |
| 1 | 素数×分拆 | `v01_prime_partition.py` | 对数导数 | ✅ n^(-1/2)衰减 |
| 5 | π×熵 | `v05_pi_entropy.py` | 系数熵分析 | ✅ 熵≈0结构化 |

## 3条幻觉归档

| # | 幻觉 | 归档状态 |
|---|------|----------|
| 3 | AGM×正规数 | 休眠，触发条件见`archive_heuristic.py` |
| 4 | MockTheta×化圆为方 | 休眠 |
| 10 | MockTheta×高合成数 | 休眠 |

## 基础设施

- `base_validation.py` — 验证框架基类
- `archive_heuristic.py` — 启发性归档管理器

## 运行

```bash
pip3 install mpmath sympy numpy
python3 v06_zeta_beta.py
python3 v08_theta_cubic.py
# ... etc
```

## 部署服务器

- 桦树工坊 (43.160.201.202) ✅
- 腾讯云2核8G (43.160.209.250) ✅
- 腾讯外网 (43.156.118.14) ✅
