from pydantic import BaseModel, HttpUrl, AnyUrl

class LinkModel(BaseModel):
    homepage: HttpUrl
    resource: AnyUrl

link: LinkModel = LinkModel(homepage="https://example.com", 
                            resource="ftp://example.com/resource")
