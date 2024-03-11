import click
import wikipedia

@click.command()
@click.option('--length',prompt='Lines of Summary',
                help='NO of lines o summary required')
@click.option('--name',prompt='Wikipedia page to scrape',
                help='Web page to want to scrape')
def scrape(name='Microsoft',length=10):
    result=wikipedia.summary(name,sentences=length)
    #click.echo(click.style(f"{result}",fg="red"))
    return result
if __name__=='__main__':
    scrape()