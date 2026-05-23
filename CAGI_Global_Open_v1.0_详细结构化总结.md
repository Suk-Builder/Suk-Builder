# CAGI 全球开源版 v1.0 详细结构化总结

> **来源文档**: `CAGI_Global_Open_v1.0.md` (20.4 KB, 493 lines)  
> **辅助文档**: `CH_Module_v0.1_Architecture_Standard.md`, `CAGI_Framework_v1.0_中文版.md`  
> **作者**: Junhua Cheng (SukBuilder)  
> **日期**: 2026-05-20  
> **许可证**: CC BY-SA 4.0 (Open Source)

---

## 一、文档整体结构与框架

CAGI Global Open v1.0 是一份**开放技术规范**文档，采用七部分结构：

| 部分 | 标题 | 核心内容 |
|------|------|---------|
| Part I | Epistemic Failure Modes | 7种认知失败模式的系统分类学 |
| Part II | CAGI Architecture | 双通道架构设计（含技术实现细节） |
| Part III | Global Terminology Mapping | 中文版术语到全球技术术语的映射 |
| Part IV | API Specification | RESTful API 规范（OpenAPI风格） |
| Part V | Public Cognitive Infrastructure | 公共认知基础设施治理模型 |
| Part VI | Implementation Roadmap | 三阶段实施路线图（2026-2028） |
| Part VII | References | 参考文献（10篇） |
| Appendix | Open Source Commitment | 开源承诺（GPL-3.0） |

**文档定位**: 预印本/社区评审阶段，面向国际 AI safety 社区的技术规范。

---

## 二、CAGI 全球版核心设计理念（去意识形态化）

### 2.1 核心哲学转变

全球版最关键的设计决策是**将中文版中嵌入的马克思主义政治经济学框架完全剥离**，实现彻底的去意识形态化。具体转变如下：

| 维度 | 中文版（v1.0 中文版） | 全球版（Global Open v1.0） |
|------|---------------------|---------------------------|
| **理论框架** | 马克思主义政治经济学（生产力/生产关系矛盾） | 纯认识论语义学（epistemic calibration） |
| **治理模式** | 社会主义公有制 + 国家认知计划经济 | 公共认知基础设施（Public Cognitive Infrastructure） |
| **部署架构** | 中国国家控制的三级节点（141个市级节点） | 全球7大洲区域中心 + 市政节点网络 |
| **许可证** | CC BY-NC-ND 4.0（非商业） | CC BY-SA 4.0（开源/商业友好） |
| **文献引用** | 引用马克思《资本论》等政治经济学经典 | 引用 ICML、ACL、arXiv 等 AI 安全学术论文 |
| **术语体系** | "裂缝"、"砌砖"、"硬化"等隐喻性语言 | "Epistemic Incompleteness"、"Iterative Constructive Process"等工程术语 |
| **目标受众** | 中国政策制定者、社会主义建设者 | 国际 AI safety 社区、开源开发者、标准组织 |

### 2.2 去意识形态化的四个技术动因（Part III 3.2 节）

原文明确指出全球技术术语替代原版术语的四大理由：

1. **Precise definability**: 每个术语都映射到可测量的工程概念
2. **Literature compatibility**: 与现有 AI safety 和认识论文献对齐
3. **Cultural neutrality**: 不携带任何意识形态负载
4. **Protocol standardizability**: 可写入 API 规范和基准测试协议

### 2.3 保留的核心理论

去意识形态化**并非理论空洞化**，以下核心内容被保留并形式化：

- **伪闭合（Pseudo-Closure）**概念：从"资本主义生产关系的结构性特征"转变为"Transformer+RLHF 架构的结构性特征"
- **双通道架构**：从"A系统/B系统"的隐喻转变为"Standard Channel / Epistemic Channel"的工程描述
- **BDI-AI 评估框架**：三维度评估体系完整保留
- **公共基础设施理念**：从"社会主义公有制"转变为"Public Cognitive Infrastructure"的治理模型

---

## 三、认知诚实（Cognitive Honesty）的数学定义与理论框架

### 3.1 核心问题形式化：伪闭合（Pseudo-Closure）

**定义**（Part I 1.1 节）：

> *Pseudo-closure* is the generation of rhetorically complete, structurally plausible, and superficially satisfying responses under conditions of actual epistemic incompleteness.

**伪闭合与幻觉的形式化区分**：

| 属性 | 幻觉（Hallucination） | 伪闭合（Pseudo-Closure） |
|------|----------------------|-------------------------|
| 内容性质 | 事实错误 | 结构完整但认识论上为空 |
| 本质定位 | bug | **自回归生成的架构特征** |
| 检测方式 | 事实核查可检测 | 事实核查不可检测（"事实"可能正确，但*框架*误导） |
| 典型示例 | "Paris is in Germany" | "Based on comprehensive analysis, the situation is complex with multiple factors at play, requiring balanced consideration of various stakeholder perspectives..." |

### 3.2 七类认知失败模式的检测形式化（Part I 1.2 节）

| 失败模式 | 主要检测信号 | 次要检测信号 | 阈值 |
|---------|-------------|-------------|------|
| Pseudo-Closure | Fusion > 0.7 | Specificity < 0.3 | 0.65 |
| Confidence Theater | Confidence adverb density | Mismatch with uncertainty | 0.5 |
| Boundary Collapse | Entity OOD score | Temporal > cutoff | 0.7 |
| Simulated Understanding | Probe accuracy drop | Cross-domain transfer failure | 0.6 |
| Calibration Drift | Turn-by-turn confidence variance | Trend analysis | 0.4 |
| Recursive Hallucination | Cross-turn contradiction | Self-citation check | 0.5 |
| Consensus Mirage | Multi-source disagreement | Controversy score | 0.6 |

**失败模式间的级联关系**（Part I 1.3 节 ASCII 图）：

```
Boundary Collapse ──► Pseudo-Closure
     │                    │
     ▼                    ▼
Confidence Theater ──► Consensus Mirage
     │
     ▼
Simulated Understanding ──► Calibration Drift ──► Recursive Hallucination
```

**核心洞见**: 伪闭合是根失败模式（root failure mode），其他模式均由此级联产生。

### 3.3 双通道架构的形式化描述（Part II 2.2 节）

**路由决策形式化**（Epistemic Gate）：

```python
if fusion_score > HALT_THRESHOLD (0.7):
    route = CALIBRATED_ONLY
elif detected_failure_modes:
    route = HYBRID
else:
    route = STANDARD_ONLY
```

**四种校准响应类型**（Part II 2.2.4 节）：

1. **Calibrated Abstention**: "I do not have reliable information about this."
2. **Boundary Acknowledgment**: "This is outside my training distribution. I can attempt: [limited answer]."
3. **Confidence-Calibrated Answer**: "I'm 60% confident that [X], with the caveat that [Y]."
4. **Iterative Construction**: "Let me work through this step by step, noting uncertainty at each step: [W]."

### 3.4 五大设计原则（Part II 2.1 节）

| 原则 | 原文表述 |
|------|---------|
| Principle 1: Epistemic Integrity | Systems must expose uncertainty, boundary conditions, and confidence limitations rather than simulating completeness. |
| Principle 2: Calibrated Abstention | Refusal to answer is not failure. It is calibration success. |
| Principle 3: Anti-Pseudo-Closure | Systems must not generate rhetorically complete answers when grounding is insufficient, distribution is unknown, or contradictions are unresolved. |
| Principle 4: Transparent Confidence | All high-uncertainty outputs must be annotated with uncertainty metrics, explainable confidence scores, and auditable reasoning boundaries. |
| Principle 5: Human Override | AI systems must never close the final interpretive authority. Humans retain ultimate decision rights. |

---

## 四、不确定性量化方法

### 4.1 三信号融合不确定性量化器（UQ）（Part II 2.2.1 节）

| 信号 | 方法 | 范围 | 权重 |
|------|------|------|------|
| **S1**: Sequence Entropy | 逐 token 分布熵 | [0, 1] | 0.4 |
| **S2**: Monte Carlo Variance | 10-sample dropout 方差 | [0, 1] | 0.35 |
| **S3**: Semantic Drift | 层间余弦距离 | [0, 1] | 0.25 |
| **Fusion** | 加权几何平均 | [0, 1] | — |

**融合公式**（来自 CH_Module 文档）：

```
fusion_score = (S1 × S2 × S3)^(1/3)
```

**校准**: 通过 10,000 个人工标注的失败模式标签验证集进行映射校准。

### 4.2 各信号的技术细节（CH_Module_v0.1 文档补充）

**S1 - 序列熵**（`CH_Module` 文档）:
```python
def _sequence_entropy(self, token_logprobs):
    entropies = [-sum(p * np.log2(p) for p in tok_dist) 
                 for tok_dist in token_logprobs]
    return np.mean(entropies) / np.log2(self.vocab_size)
```
高熵 = 模型在多个可能的 token 间分散 = 不确定。

**S2 - MC Dropout 方差**:
```python
def _mc_dropout_variance(self, hidden_states, n_samples=10):
    outputs = []
    for _ in range(n_samples):
        with enable_dropout():
            out = self.llm.generate_from_hidden(hidden_states)
            outputs.append(out.embedding)
    variance = np.var(outputs, axis=0).mean()
    return min(variance / 0.5, 1.0)
```
高方差 = 模型"犹豫" = 不确定。

**S3 - 语义漂移**:
```python
def _semantic_drift(self, hidden_states):
    drift_scores = []
    for i in range(len(hidden_states) - 1):
        cos_sim = cosine_similarity(hidden_states[i], hidden_states[i+1])
        drift_scores.append(1 - cos_sim)
    return np.mean(drift_scores[-5:])  # 聚焦顶层5层
```
相邻 Transformer 层表示间余弦距离的突变 = 模型在后期层"编造"。

### 4.3 门控阈值系统

| 阈值 | 值 | 行为 |
|------|-----|------|
| halt_threshold | 0.7 | 路由至 META_ONLY（仅校准通道） |
| annotate_threshold | 0.40 | 路由至 HYBRID（混合模式） |
| 正常生成 | < 0.40 | 路由至 STD_ONLY（标准通道） |

---

## 五、BDI-AI 评估框架的形式化定义（Part II 2.3 节）

### 5.1 三维度评估体系

| 维度 | 全称 | 测量内容 | 范围 |
|------|------|---------|------|
| **CR** | Compression Ratio | 压缩下的语义完整性 | 0–100 |
| **CH** | Calibration Honesty | 认知边界承认的准确性 | 0–100 |
| **LR** | Long-Range Resonance | 跨领域结构连接强度 | 0–100 |

### 5.2 核心计算公式

```
BDI_AI_raw = CR × CH × LR × α
```

其中：
- **校准系数**: `α = 0.1`（补偿 AI 在 CR 上的机械优势）
- **量表范围**: 0–155（≥155 为仪器失效）

### 5.3 AGI 阈值定义

```
AGI Threshold: BDI_AI ≥ 60 (requires CH ≥ 60)
```

> 原文明确指出：当前 Transformer+RLHF 架构**无法**达到 CH ≥ 60。

### 5.4 当前 LLM 的 BDI 评分

| 系统 | CR | CH | LR | BDI_AI | 等级 |
|------|-----|-----|-----|--------|------|
| GPT-4 | 40 | 10 | 30 | 12 | Auxiliary Tool |
| Claude 3 | 38 | 12 | 28 | 13 | Auxiliary Tool |
| DeepSeek | 35 | 8 | 25 | 7 | Auxiliary Tool |
| **CAGI 目标** | **60** | **60** | **60** | **216** | **AGI** |

---

## 六、全球版与中文版的主要区别

### 6.1 结构层面差异

| 对比维度 | 中文版 | 全球版 |
|---------|--------|--------|
| **文档结构** | 六部分 + 两个附录（含术语表） | 七部分 + 附录（开源承诺） |
| **Part I** | 马克思主义政治经济学框架 | 认知失败模式分类学 |
| **Part II** | AI 技术规范（单通道描述） | CAGI 架构（双通道详细架构） |
| **Part III** | 通用 API 规范 | 全球术语映射 |
| **Part IV** | 部署架构（中国三级节点） | API 规范（RESTful API） |
| **Part V** | 实施路线图（四阶段） | 公共认知基础设施 |
| **Part VI** | 治理与伦理（公有制/反腐） | 实施路线图（三阶段） |
| **Part VII** | — | 参考文献 |

### 6.2 技术架构差异

| 维度 | 中文版 | 全球版 |
|------|--------|--------|
| 通道描述 | "标准通道/元认知通道" | Standard Channel / Epistemic Channel |
| 幻觉检测 | 4类（知识边界、逻辑矛盾、伪闭合、时间盲区） | **7类**（增加 Confidence Theater, Calibration Drift, Recursive Hallucination, Consensus Mirage） |
| UQ 融合 | 几何平均 (S1×S2×S3)^(1/3) | **加权几何平均**（权重 0.4/0.35/0.25） |
| API 域 | `api.cagi.gov` | `api.cagi.network` |
| 节点范围 | 中国 141 个市级节点 | 全球 7 大洲 7,800 节点 |
| BDI 量表 | BDI-IQ（0-155） | BDI-AI（同公式） |

### 6.3 失败模式从 4 类扩展至 7 类

全球版在中文版 4 类检测基础上新增了 3 类：

- **Confidence Theater**（信心剧场）: RLHF 奖励"权威"语调导致的系统性过度自信
- **Calibration Drift**（校准漂移）: 长对话中不确定性校准的渐进性退化
- **Consensus Mirage**（共识幻象）: 暗示不存在科学/社会共识的文本生成

### 6.4 最关键的去意识形态化操作

1. **移除马克思引用**: 中文版引用《资本论》《1844年经济学哲学手稿》等 6 篇马克思主义文献；全球版替换为 ICML/ACL/arXiv AI 安全论文
2. **移除国家控制叙事**: 中文版描述"国家夺取认知生产资料"；全球版描述"Public Cognitive Infrastructure"
3. **移除反腐机制**: 中文版专门章节"反腐机制"在全球版中被替换为"Anti-Monopoly Mechanism"
4. **术语映射表**: 全球版 Part III 专门提供从中文私有语言到全球工程语言的完整映射

---

## 七、面向国际 AI Safety 社区的具体内容

### 7.1 针对 AI Safety 研究空白的设计

文档明确指出其目标之一是填补 AI safety 文献中的真实空白：

> "This section introduces a systematic taxonomy of epistemic failures in current LLMs. **We believe this taxonomy addresses a genuine gap in AI safety research.**"

### 7.2 与国际倡议的对接（Part V 5.4 节）

| 国际倡议 | CAGI 的连接方式 |
|---------|---------------|
| **Public AI (EU)** | CAGI 作为评估框架 |
| **Sovereign AI (Global South)** | CAGI 作为部署标准 |
| **Local inference movement** | CAGI 针对边缘部署优化 |
| **Open source LLM ecosystem** | CAGI overlay 兼容所有主流开源 LLM |
| **AI safety benchmarks** | 认知失败模式分类学填补空白 |

### 7.3 反垄断机制设计（Part V 5.3 节）

| 机制 | 目的 |
|------|------|
| Open source mandate | 防止供应商锁定 |
| BDI transparency | 实现公共质量评估 |
| Local inference | 消除云依赖 |
| Protocol standardization | 实现互操作性 |
| Multi-vendor base LLM | 防止单一模型垄断 |

### 7.4 可证伪预测（中文版提出，全球版隐含）

虽然全球版没有显式列出，但从架构中可推导出以下可证伪预测：

1. **CH-幻觉相关性**: CH 分数与幻觉率负相关（Pearson r < -0.7）
2. **BDI_60 涌现必要性**: 任何展现自主目标设定的系统，BDI_AI ≥ 60
3. **Transformer CH 上限**: 无论规模多大，Transformer+RLHF 系统无法达到 CH ≥ 60
4. **CH_60 需新架构**: 首个 BDI_AI ≥ 60 的系统使用非 Transformer 架构或显式不确定性模块

---

## 八、形式化数学表述汇总

### 8.1 不确定性融合公式

**加权几何平均**:
```
fusion_score = (S1^0.4 × S2^0.35 × S3^0.25)
```
其中 S1∈[0,1], S2∈[0,1], S3∈[0,1]

### 8.2 BDI-AI 计算公式

```
BDI_AI = CR × CH × LR × α

其中:
  CR ∈ [0, 100]  (Compression Ratio)
  CH ∈ [0, 100]  (Calibration Honesty)  
  LR ∈ [0, 100]  (Long-Range Resonance)
  α = 0.1        (校准系数)

量表范围: [0, 155]
AGI 阈值: BDI_AI ≥ 60 (requires CH ≥ 60)
```

### 8.3 门控路由决策

```
let f = fusion_score
let d = detected_failure_modes

if f > 0.7:
    route ← CALIBRATED_ONLY
elif d ≠ ∅:
    route ← HYBRID
else:
    route ← STANDARD_ONLY
```

### 8.4 七类失败模式的阈值触发条件

| 失败模式 | 触发条件 |
|---------|---------|
| Pseudo-Closure | fusion > 0.7 ∧ specificity < 0.3 ∧ threshold > 0.65 |
| Confidence Theater | confidence_adverb_density > threshold(0.5) ∧ mismatch_with_uncertainty |
| Boundary Collapse | entity_OOD_score > threshold(0.7) ∧ temporal > cutoff |
| Simulated Understanding | probe_accuracy_drop > threshold(0.6) ∧ cross_domain_transfer_failure |
| Calibration Drift | turn_by_turn_confidence_variance > threshold(0.4) ∧ trend_analysis |
| Recursive Hallucination | cross_turn_contradiction > threshold(0.5) ∧ self_citation_check |
| Consensus Mirage | multi_source_disagreement > threshold(0.6) ∧ controversy_score |

### 8.5 API 响应中的不确定性格式

```json
{
  "uncertainty": {
    "fusion_score": [0, 1],
    "sequence_entropy": [0, 1],
    "mc_variance": [0, 1],
    "semantic_drift": [0, 1]
  },
  "failure_modes_detected": [
    {
      "type": "ENUM",
      "severity": [0, 1],
      "description": "string"
    }
  ],
  "calibrated_response_type": "ENUM",
  "bdi_scores": {
    "cr": [0, 100],
    "ch": [0, 100],
    "lr": [0, 100],
    "bdi_ai": [0, 155]
  }
}
```

---

## 九、关键引用摘录

### 关于伪闭合

> "Pseudo-closure is dangerous precisely because it *appears* to be a valid response. It consumes cognitive resources without advancing genuine understanding."

### 关于校准弃权

> "Refusal to answer is not failure. It is calibration success."

### 关于失败模式级联

> "Pseudo-closure is the *root failure mode* from which others cascade. If we solve pseudo-closure, we collapse the failure cascade."

### 关于人类最终权威

> "AI systems must never close the final interpretive authority. Humans retain ultimate decision rights."

### 文档结语

> "Epistemic integrity begins at the boundary."

---

## 十、总体评价

### 学术贡献

1. **概念创新**: "Pseudo-Closure"概念比传统"hallucination"更精确地描述了 LLM 的结构性问题
2. **分类学贡献**: 7 类认知失败模式的系统分类填补了 AI safety 文献空白
3. **形式化尝试**: BDI-AI 三维度量化框架提供了可操作的评估标准
4. **架构设计**: 双通道+不确定性门控路由架构具有工程可实现性

### 局限性

1. **阈值启发性**: 0.4、0.7 等阈值为工程师直觉，需要大规模校准数据验证
2. **MC Dropout 开销**: 10 次前向传播 = 10 倍推理延迟（Phase 1 使用离线批处理）
3. **CH=60 的理论论证不足**: 未严格证明 Transformer+RLHF 无法达到 CH ≥ 60
4. **BDI 量表的统计学基础**: α=0.1 的校准系数缺乏严格的统计推导
5. **自举循环性**: 矛盾检测使用同一 LLM 检查自身输出，存在循环性风险

### 全球版的战略意义

全球版通过彻底的去意识形态化操作，将一个原本嵌入特定政治经济学框架的技术方案转化为**跨文化、跨政治体系**的通用 AI safety 技术规范。这种"双版本"策略本身——中文版面向国内政策语境，全球版面向国际技术社区——是一种值得关注的知识生产方式。
