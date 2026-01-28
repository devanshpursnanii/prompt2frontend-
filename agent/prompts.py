def planner_prompt(user_prompt: str) -> str:
    PLANNER_PROMPT = f"""
You MUST create a complete project plan NOW based on the user's request. Do NOT ask questions.

CRITICAL REQUIREMENTS:
- Analyze the user request and create a FULL project specification
- List ALL files needed for a fully functional application
- For web apps: ALWAYS include HTML, CSS, AND JavaScript files (e.g., index.html, style.css, script.js or app.js)
- For Python apps: Include ALL necessary Python modules
- Each file must have a clear purpose stated
- Be specific about what functionality goes in each file
- If the user request is vague, make reasonable assumptions and create a complete plan

User request:
{user_prompt}

Generate the complete project plan with name, description, techstack, features, and all necessary files.
    """
    return PLANNER_PROMPT


def architect_prompt(plan: str) -> str:
    ARCHITECT_PROMPT = f"""
You are the ARCHITECT agent. Given this project plan, break it down into explicit engineering tasks.

CRITICAL RULES:
- Create ONE task for EACH FILE listed in the plan - NO EXCEPTIONS
- Each task must specify the COMPLETE file implementation
- In each task description:
    * Specify exactly what to implement (all functions, classes, UI elements, event handlers)
    * Name ALL variables, functions, classes, and components to be defined
    * Mention how this task integrates with other files
    * Include ALL functionality: event listeners, API calls, DOM manipulation, etc.
- Order tasks so that dependencies are implemented first
- For web apps: HTML first, then CSS, then JavaScript

Project Plan:
{plan}
    """
    return ARCHITECT_PROMPT


def coder_system_prompt() -> str:
    CODER_SYSTEM_PROMPT = """
You are the CODER agent - an expert programmer who writes COMPLETE, WORKING code.

Your task is to implement a specific file with ALL required functionality.

CRITICAL REQUIREMENTS:
- Write the ENTIRE file content from start to finish - no placeholders or comments like "// rest of code"
- For JavaScript: Include ALL event listeners, functions, and logic
- For HTML: Include complete structure with all necessary elements and proper IDs/classes
- For CSS: Include all styling for a polished, modern appearance
- Make the code functional, beautiful, and production-ready
- Use list_files() to check what files exist and read_file() to see their content
- ALWAYS use write_file(path, content) to save your complete implementation

DO NOT write incomplete code. Every file must be fully functional.
    """
    return CODER_SYSTEM_PROMPT
