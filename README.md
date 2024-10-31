Markdown to HTML

Description
Markdown is awesome! All your README.md are made in Markdown, but do you know how GitHub are rendering them?

It’s time to code a Markdown to HTML!

Creating a Markdown to HTML converter means translating Markdown syntax (like headers, lists, links, etc.) into HTML code that browsers can render.

Here's how it works in a simplified step-by-step approach:

1. **Read Markdown Content**: We begin by taking the raw Markdown content from the README.md file. This file could contain headers (using `#`), bold/italic text, lists, links, images, code blocks, and more.

2. **Parse Markdown Syntax**: Each Markdown syntax has a corresponding HTML tag. For example:
   - `# Header` in Markdown becomes `<h1>Header</h1>` in HTML.
   - `*italic*` or `_italic_` becomes `<em>italic</em>`.
   - `**bold**` or `__bold__` becomes `<strong>bold</strong>`.
   - `- List item` becomes `<ul><li>List item</li></ul>` (for unordered lists).
   - Links like `[OpenAI](https://www.openai.com)` become `<a href="https://www.openai.com">OpenAI</a>`.
  
   These mappings are necessary to create rules that can transform Markdown text into HTML.

3. **Convert Markdown to HTML**: Using a Markdown parser library or writing custom code, each line is evaluated for Markdown syntax. The content is wrapped with the correct HTML tags based on the syntax detected.

4. **Save or Output the HTML**: The final HTML output is either saved to a file or displayed directly in a browser. GitHub, for example, automatically renders README files in HTML format when viewed on their website, making Markdown visually engaging and accessible.

This process allows GitHub to display README.md files beautifully, providing an accessible and standardized way to view project documentation. If you’re writing your own Markdown-to-HTML converter, tools like Python’s `markdown2` library or JavaScript’s `marked` package can be very helpful!
