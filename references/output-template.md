# Output Template

Use this template for normal ideation outputs.

```markdown
**资料里的机会地图**
- 高频痛点：
- 重复流程：
- 信息差：
- 决策困难：
- 可工具化节点：

**Top 10 小产品机会**
1. 名称：一句话说明；用户；产品形态；输入 -> 输出；信号强度：高/中/低。
2. ...

**淘汰的想法**
- 名称：淘汰原因；失败检查：来源支撑/迁移性/产品清晰度/可构建性。
- 名称：淘汰原因；失败检查：来源支撑/迁移性/产品清晰度/可构建性。

**Top 3 候选**
对每个候选重复以下完整记录，不得用一段总结替代：

1. 名称：
   ID：
   用户：
   购买者假设：未知/假设对象
   场景：
   痛点：
   当前替代方案：
   产品形态：
   输入：
   输出：
   来源事实：
   AI 推断：
   为什么现在：
   未验证假设：
   来源置信度：高/中/低
   验证：来源支撑 true/false；迁移性 true/false；产品清晰度 true/false
   状态：verified/rejected
   淘汰原因：仅 rejected 填写
   压力测试：最强触发 / 最强反对理由 / 边界场景 / 决策

**交给 business-lens 的候选**
复用上方完整 Top 3 记录作为交接，不得只写结论摘要。机器可读或保存场景使用以下结构：

schema_version: idea-opportunity/v1
id:
name:
user:
buyer: unknown
scene:
pain:
current_workaround:
product_shape:
input:
output:
source_support:
  -
inferences:
  -
uncertainties:
  -
why_now:
confidence:
validation:
  source_support: true
  transferability: true
  product_sharpness: true
status: verified
rejection_reason: ""
```

Keep outputs concise unless the user asks for a full report.
