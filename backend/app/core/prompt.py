"""
LLM prompt engineering and PRD generation logic
"""

import logging
from typing import Dict, Any
from app.core.model import GenerateResponse

logger = logging.getLogger(__name__)

# System prompt for PRD generation
SYSTEM_PROMPT = """You are an expert product manager and technical architect. Your role is to generate comprehensive Product Requirement Documents (PRDs) from product ideas.

For each product idea, you must provide:
1. A clear problem statement and executive summary
2. Detailed user stories and key features
3. A realistic 30/60/90-day development roadmap
4. High-level technical architecture recommendations

Be specific, actionable, and professional. Focus on feasibility and user value."""

def create_prd_prompt(idea: str) -> str:
    """
    Create a structured prompt for PRD generation
    
    Args:
        idea: The product idea description
        
    Returns:
        Formatted prompt string
    """
    return f"""Generate a comprehensive Product Requirement Document for the following product idea:

PRODUCT IDEA:
{idea}

Please provide a detailed PRD with the following structure:

1. EXECUTIVE SUMMARY & PROBLEM STATEMENT
   - What problem does this solve?
   - Who are the target users?
   - What is the value proposition?

2. USER STORIES & KEY FEATURES
   - List 5-8 user stories in the format: "As a [user type], I want [goal] so that [benefit]"
   - Include specific features that address these stories
   - Prioritize features by importance

3. DEVELOPMENT ROADMAP
   - 30-day milestone: Core MVP features
   - 60-day milestone: Enhanced functionality
   - 90-day milestone: Advanced features and optimization
   
4. TECHNICAL ARCHITECTURE
   - Recommended tech stack (frontend, backend, database)
   - Key architectural decisions
   - Scalability considerations
   - Third-party integrations if needed

Be specific, realistic, and actionable."""

async def call_llm(prompt: str, system_prompt: str) -> str:
    """
    Call the LLM API to generate PRD content
    
    TODO: Implement actual LLM integration
    Options:
    - OpenAI: https://platform.openai.com/docs/api-reference
    - Anthropic Claude: https://docs.anthropic.com/claude/reference/
    - Other providers
    
    Args:
        prompt: The user prompt
        system_prompt: The system prompt
        
    Returns:
        Generated text from the LLM
    """
    # TODO: Replace with actual LLM API call
    # Example OpenAI implementation:
    # import openai
    # response = await openai.ChatCompletion.acreate(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": system_prompt},
    #         {"role": "user", "content": prompt}
    #     ],
    #     temperature=0.7
    # )
    # return response.choices[0].message.content
    
    # Example Anthropic implementation:
    # import anthropic
    # client = anthropic.AsyncAnthropic(api_key="your-api-key")
    # message = await client.messages.create(
    #     model="claude-3-5-sonnet-20241022",
    #     max_tokens=2000,
    #     system=system_prompt,
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # return message.content[0].text
    
    logger.info("Using placeholder LLM response")
    
    # Placeholder response for testing
    return """1. EXECUTIVE SUMMARY & PROBLEM STATEMENT

This product addresses the critical challenge of maintaining healthy hydration habits in our busy modern lives. Many people struggle to drink enough water throughout the day, leading to decreased energy, poor concentration, and health issues. Our target users are health-conscious individuals aged 18-45 who want to improve their wellness but need motivation and tracking tools. The value proposition is simple: make hydration tracking effortless, engaging, and social through gamification and smart reminders.

2. USER STORIES & KEY FEATURES

- As a busy professional, I want automated reminders to drink water so that I don't forget during work hours
- As a fitness enthusiast, I want to adjust my hydration goals based on activity level so that I stay properly hydrated during workouts
- As a competitive person, I want to see how my hydration compares to friends so that I stay motivated
- As a data-driven user, I want to see trends in my hydration over time so that I can identify patterns
- As a forgetful user, I want quick one-tap logging so that tracking doesn't feel like a chore
- As a goal-oriented person, I want to earn achievements and badges so that I feel rewarded for consistency
- As a visual learner, I want clear graphics showing my progress so that I can quickly understand my status
- As a health-conscious user, I want personalized recommendations based on weather and activity so that my goals stay relevant

3. DEVELOPMENT ROADMAP

30-Day Milestone (MVP):
- User authentication and onboarding
- Basic water intake logging with simple tap interface
- Daily goal setting with standard recommendations
- Push notification system for hydration reminders
- Simple progress visualization (daily chart)
- Basic profile and settings management

60-Day Milestone (Enhanced):
- Gamification system with points and achievements
- Social features: friend connections and leaderboards
- Advanced analytics with weekly/monthly trends
- Customizable reminder schedules
- Widget support for quick logging
- Integration with Apple Health and Google Fit
- Dark mode and UI enhancements

90-Day Milestone (Advanced):
- Smart recommendations based on weather and activity
- Wearable device integration (Apple Watch, Fitbit)
- Challenges and competitions with friends
- Premium subscription tier with advanced analytics
- Export data functionality
- Multi-language support
- Performance optimization and offline mode

4. TECHNICAL ARCHITECTURE

Frontend:
- React Native for cross-platform mobile development (iOS and Android)
- Redux for state management
- React Navigation for routing
- Native modules for push notifications and background tasks

Backend:
- Node.js with Express.js for RESTful API
- PostgreSQL for relational data (users, logs, friendships)
- Redis for caching and session management
- Bull for job queues (notification scheduling)
- Socket.io for real-time features (leaderboards)

Infrastructure:
- AWS/GCP for hosting with auto-scaling
- S3 for avatar and asset storage
- CloudWatch/Stackdriver for monitoring
- CI/CD with GitHub Actions
- Docker containers for consistent deployments

Key Architectural Decisions:
- Microservices approach for scalability (auth, logging, notifications, social)
- Event-driven architecture for real-time updates
- Horizontal scaling for API servers
- Database read replicas for analytics queries
- CDN for static assets

Third-Party Integrations:
- Firebase Cloud Messaging for push notifications
- OAuth 2.0 for social login (Google, Apple)
- Stripe for payment processing (premium tier)
- Weather API for contextual recommendations
- Health kit integrations for wearable data"""

def parse_llm_response(llm_output: str) -> Dict[str, Any]:
    """
    Parse the LLM output into structured PRD components
    
    Args:
        llm_output: Raw text output from the LLM
        
    Returns:
        Dictionary with structured PRD data
    """
    # Simple parser - can be enhanced with more sophisticated logic
    lines = llm_output.split('\n')
    
    summary_lines = []
    feature_lines = []
    roadmap_lines = []
    architecture_lines = []
    
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
            
        # Detect section headers
        if "EXECUTIVE SUMMARY" in line.upper() or "PROBLEM STATEMENT" in line.upper():
            current_section = "summary"
            continue
        elif "USER STORIES" in line.upper() or "KEY FEATURES" in line.upper():
            current_section = "features"
            continue
        elif "ROADMAP" in line.upper() or "DEVELOPMENT ROADMAP" in line.upper():
            current_section = "roadmap"
            continue
        elif "ARCHITECTURE" in line.upper() or "TECHNICAL ARCHITECTURE" in line.upper():
            current_section = "architecture"
            continue
        
        # Skip numbered section headers like "1.", "2.", etc.
        if line and line[0].isdigit() and '.' in line[:3]:
            continue
            
        # Add content to appropriate section
        if current_section == "summary":
            summary_lines.append(line)
        elif current_section == "features":
            feature_lines.append(line)
        elif current_section == "roadmap":
            roadmap_lines.append(line)
        elif current_section == "architecture":
            architecture_lines.append(line)
    
    # Process summary
    summary = '\n'.join(summary_lines) if summary_lines else "Product requirement document generated successfully."
    
    # Process features - extract lines with user stories or feature markers
    features = []
    for line in feature_lines:
        if line and (line.startswith('-') or line.startswith('•') or 'As a' in line or 'Feature:' in line):
            features.append(line.lstrip('-•').strip())
    if not features:
        features = ["Feature specifications to be detailed"]
    
    # Process roadmap - extract milestone lines
    roadmap = []
    for line in roadmap_lines:
        if line and ('day' in line.lower() or 'milestone' in line.lower() or line.startswith('-')):
            roadmap.append(line.lstrip('-•').strip())
    if not roadmap:
        roadmap = ["30 Days: Initial development", "60 Days: Feature expansion", "90 Days: Optimization and launch"]
    
    # Process architecture
    architecture = '\n'.join(architecture_lines) if architecture_lines else "Technical architecture to be defined based on requirements."
    
    return {
        "summary": summary,
        "features": features,
        "roadmap": roadmap,
        "architecture": architecture
    }

async def generate_prd(idea: str) -> GenerateResponse:
    """
    Main function to generate a PRD from an idea
    
    Args:
        idea: The product idea description
        
    Returns:
        GenerateResponse with structured PRD data
    """
    try:
        # Create the prompt
        prompt = create_prd_prompt(idea)
        
        # Call LLM (currently placeholder)
        llm_output = await call_llm(prompt, SYSTEM_PROMPT)
        
        # Parse the output
        prd_data = parse_llm_response(llm_output)
        
        # Return structured response
        return GenerateResponse(**prd_data)
        
    except Exception as e:
        logger.error(f"Error in generate_prd: {e}", exc_info=True)
        raise