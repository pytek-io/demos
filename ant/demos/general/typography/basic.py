from reflect_html import *
from reflect_antd import Typography, Divider

Title, Paragraph, Text, Link = (
    Typography.Title,
    Typography.Paragraph,
    Typography.Text,
    Typography.Link,
)

blockContent = "AntV 是蚂蚁金服全新一代数据可视化解决方案，致力于提供一套简单方便、专业可靠、不限可能的数据可视化最佳实践。得益于丰富的业务场景和用户需求挑战，AntV 经历多年积累与不断打磨，已支撑整个阿里集团内外 20000+ 业务系统，通过了日均千万级 UV 产品的严苛考验。 我们正在基础图表，图分析，图编辑，地理空间可视化，智能可视化等各个可视化的领域耕耘，欢迎同路人一起前行"


def app():
    return Typography(
        [
            Title("Introduction"),
            Paragraph(
                "In the process of internal desktop applications development, many different design specs and implementations would be involved, which might cause designers and developers difficulties and duplication and reduce the efficiency of development."
            ),
            Paragraph(
                [
                    "After massive project practice and summaries, Ant Design, a design language for background applications, is refined by Ant UED Team, which aims to ",
                    Text(
                        "uniform the user interface specs for internal background projects, lower the unnecessary cost of design differences and implementation and liberate the resources of design and front-end development",
                        strong=True,
                    ),
                    ".",
                ]
            ),
            Title("Guidelines and Resources", level=2),
            Paragraph(
                [
                    "We supply a series of design principles, practical patterns and high quality design resources, ",
                    Text("Sketch", code=True),
                    "and",
                    Text("Axure", code=True),
                    "to help people create their product prototypes beautifully and efficiently.",
                ]
            ),
            Paragraph(
                ul(
                    [
                        li(Link("Principles", href="/docs/spec/proximity")),
                        li(Link("Patterns", href="/docs/spec/overview")),
                        li(Link("Resource Download", href="/docs/resources")),
                    ]
                )
            ),
            Paragraph(
                [
                    "Press",
                    Text("Esc", keyboard=True),
                    "to exit...",
                ]
            ),
            Divider(),
            Title("介绍"),
            Paragraph(
                "蚂蚁的企业级产品是一个庞大且复杂的体系。这类产品不仅量级巨大且功能复杂，而且变动和并发频繁，常常需要设计与开发能够快速的做出响应。同时这类产品中有存在很多类似的页面以及组件，可以通过抽象得到一些稳定且高复用性的内容。"
            ),
            Paragraph(
                [
                    "随着商业化的趋势，越来越多的企业级产品对更好的用户体验有了进一步的要求。带着这样的一个终极目标，我们（蚂蚁金服体验技术部）经过大量的项目实践和总结，逐步打磨出一个服务于企业级产品的设计体系 Ant Design。基于",
                    Text("『确定』和『自然』", mark=True),
                    "的设计价值观，通过模块化的解决方案，降低冗余的生产成本，让设计者专注于",
                    Text("更好的用户体验", strong=True),
                    "。",
                ]
            ),
            Title("设计资源", level=2),
            Paragraph(
                [
                    "我们提供完善的设计原则、最佳实践和设计资源文件（",
                    Text("Sketch", code=True),
                    "和",
                    Text("Axure", code=True),
                    "），来帮助业务快速设计出高质量的产品原型。",
                ]
            ),
            Paragraph(
                ul(
                    [
                        li(Link("设计原则", href="/docs/spec/proximity-cn")),
                        li(Link("设计模式", href="/docs/spec/overview-cn")),
                        li(Link("设计资源", href="/docs/resources-cn")),
                    ]
                )
            ),
            Paragraph([blockquote(blockContent), pre(blockContent)]),
            Paragraph(["按", Text("Esc", keyboard=True), "键退出阅读……"]),
        ]
    )
