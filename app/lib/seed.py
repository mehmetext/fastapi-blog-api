from sqlalchemy.ext.asyncio import AsyncSession
from app.models.post import Post
from app.controllers.blog import BlogController
from app.models.post import PostCreate


async def seed_posts(db: AsyncSession):
    sample_posts = [
        PostCreate(
            title="İlk Blog Yazısı",
            content="Bu bizim ilk blog yazımızın içeriğidir.",
            author_id=1,
        ),
        PostCreate(
            title="Python'da Asenkron Programlama",
            content="Asenkron programlama hakkında detaylı bir yazı.",
            author_id=1,
        ),
        PostCreate(
            title="FastAPI ile RESTful API Geliştirme",
            content="FastAPI kullanarak nasıl hızlı ve etkili API'ler geliştirebileceğinizi öğrenin.",
            author_id=2,
        ),
        PostCreate(
            title="Veritabanı Tasarımı İpuçları",
            content="Etkili veritabanı tasarımı için önemli ipuçları ve en iyi uygulamalar.",
            author_id=2,
        ),
        PostCreate(
            title="Web Güvenliği: OWASP Top 10",
            content="Web uygulamalarınızı güvende tutmak için bilmeniz gereken en önemli güvenlik riskleri.",
            author_id=3,
        ),
        PostCreate(
            title="Docker Konteynerları: Başlangıç Rehberi",
            content="Docker konteynerlarını anlamak ve kullanmaya başlamak için kapsamlı bir rehber.",
            author_id=3,
        ),
        PostCreate(
            title="Makine Öğrenimi Temelleri",
            content="Makine öğreniminin temel kavramları ve popüler algoritmaları hakkında bir giriş.",
            author_id=4,
        ),
        PostCreate(
            title="Git ve GitHub: Versiyon Kontrolü",
            content="Git ve GitHub kullanarak etkili versiyon kontrolü ve işbirliği yapma teknikleri.",
            author_id=4,
        ),
        PostCreate(
            title="Responsive Web Tasarımı",
            content="Farklı cihazlarda mükemmel görünen web siteleri oluşturmak için responsive tasarım ilkeleri.",
            author_id=5,
        ),
        PostCreate(
            title="Siber Güvenlik: Etik Hacking",
            content="Etik hacking ve penetrasyon testleri hakkında temel bilgiler ve uygulamalar.",
            author_id=5,
        ),
    ]

    for post in sample_posts:
        await BlogController.create_post(db, post)
