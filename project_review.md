# Student Content Recommendation Website - Complete Project Review

## 📋 PROJECT SUMMARY
**Name**: Student Content Recommendation Website  
**Purpose**: Personalized news, YouTube videos, and research paper recommendations for students  
**Target Users**: Students  
**Platforms**: Web (responsive for mobile & desktop)  
**Tech Stack**: React + Django + PostgreSQL  

---

## 🔐 PART 1: AUTHENTICATION & ACCOUNT MANAGEMENT

### Landing Page
- Display website information and policies
- "Sign Up" call-to-action button

### Sign-Up Flow
- Email field
- Password field ()
- Store email + password hash in database
- Redirect to interest selection

### Interest Selection (First-Time Only)
- Checkboxes for multiple domain selection:
  - Computer Science
  - Agriculture
  - Engineering
  - Medical
  - Business
  - Law
  - Arts
  - Science
  - Technology
  - Others
- Users can select multiple interests
- Store selections in database

### Login Flow
- Email + Password authentication
- Redirect to dashboard on success

---

## 🎨 PART 2: DASHBOARD LAYOUT

### Header Section
- **Search Bar** (top center/left)
  - Global search across all content types
  - Real-time suggestions as user types
- **User Profile Icon** (top-right)
  - Dropdown menu with: Profile, Settings, Logout

### Left Sidebar Navigation Menu
Five categories:
1. **Home** → All recommendations (mixed content)
2. **Videos** → YouTube videos only
3. **Books** → Research papers & books only
4. **News** → News articles only
5. **Articles** → Articles/blog posts only
6. **library** → User created folders

### Main Content Area

#### Filters & Sorting Section
**Date Range Filter:**
- Last 24 hours
- Last 7 days (week)
- Last 30 days (month)
- All time
- Custom date range (optional)

**Sort By Options:**
- Trending (popular + relevant combined)
- Newest (most recent first)
- Most Popular (by views/likes/saves)
- Most Relevant (to user interests)

#### Content Display Formats

**For Videos (YouTube Style):**
- Grid layout with thumbnails
- Each video shows:
  - Video thumbnail image
  - Video title
  - Channel/source name
  - View count
  - Video duration
  - Publication date
- Hover effect for preview

**For News & Articles (Wikipedia/Medium Style):**
- List or card layout
- Each item shows:
  - Thumbnail image (left or top)
  - Article headline/title
  - Source name
  - Publication date
  - Short excerpt (100-150 words)
  - "Read More" link

**For Research Papers/Books:**
- Card layout
- Each item shows:
  - Paper/book cover thumbnail
  - Title
  - Authors
  - Publication year
  - Brief description
  - "View Full"/"Download" link

---

## ❤️ PART 3: USER ENGAGEMENT FEATURES

### Like/Favorite Items
- Heart icon on each item
- Click to like/unlike
- Visual feedback (filled red heart when liked)
- Used for improving recommendations
- Tracked in database

### Save Items for Later
- Bookmark/save icon on each item
- Click to save/unsave
- Saved items appear in "Saved Items" page
- Save date tracked

### View Full Content
- "Read More" or "View Full" link on each item
- Opens full content (external link to original source)
- Click tracked in database for engagement metrics

### Engagement Tracking
- System records:
  - What items user views
  - How long they spend on items
  - Which items they like
  - Which items they save
  - Search queries they enter
- Data used to improve future recommendations

---

## 📊 PART 4: RECOMMENDATION ALGORITHM

### Ranking Formula
```
Recommendation Score = 
  (Relevance Score × 0.4) + 
  (Popularity Score × 0.3) + 
  (Recency Score × 0.3)
```

### Scoring Components

**Relevance Score (0-100 points)**
- Compares item topics/tags with user's selected interests
- Uses text similarity (cosine similarity on content vectors)
- Higher score = better match with user interests

**Popularity Score (0-100 points)**
- Based on total views, likes, saves of the item
- Normalized by item age
- Trending items score higher

**Recency Score (0-100 points)**
- Newer items get higher scores
- Older items decay gradually
- Most recent items rank highest

### Result
Items ranked by combined score → most relevant + popular + recent shown first

---

## 👤 PART 5: USER PROFILE PAGE

### Display Information
- User email address
- Selected interest domains (editable)
- Account creation date

### Profile Actions/Buttons
1. **Change Password** → Modal form to update password
2. **View Saved Items** → Link to saved items collection
3. **View Favorite Items** → Link to favorites collection
4. **Logout** → Sign out from account
5. **Delete Account** → Permanently delete account (with confirmation)

---

## 📌 PART 6: SAVED ITEMS PAGE

### Display
- Grid/list view of all items user has saved
- Show save date on each item
- Filter options:
  - By content type (Videos, News, Articles, Books)
  - By date range
- Sort options:
  - Newest saved first
  - Oldest saved first
  - Alphabetical

### Actions
- Click item to view full details
- Remove from saved (unsave button)
- Like/favorite items from this page
- Open original content

---

## ⭐ PART 7: FAVORITE ITEMS PAGE

### Display
- Grid/list view of all items user has liked
- Show date item was liked
- Filter options:
  - By content type (Videos, News, Articles, Books)
  - By date range
- Sort options:
  - Newest liked first
  - Oldest liked first
  - Alphabetical

### Actions
- Click item to view full details
- Unlike/remove from favorites (unlike button)
- Save items to saved collection from this page
- Open original content

---

## ⚙️ PART 8: SETTINGS PAGE

### 1. Account Settings Section
- Display current email address
- Option to change email
- Option to change password
- Two-factor authentication (optional for v2)

### 2. Preference Settings Section
- Update interest domains (edit categories selected at sign-up)
- Preferred content types (prioritize certain types)
- Language preference (English, Hindi, etc.)

### 3. Notification Settings Section
- Toggle notifications ON/OFF
- Notification frequency options:
  - Daily digest
  - Weekly digest
  - Real-time notifications
- Notification types to receive:
  - New recommendations matching interests
  - Trending/popular content
  - Updates on saved items

### 4. Privacy & Data Section
- Explanation of data collection practices
- Toggle: Track search history (ON/OFF)
- Toggle: Track view history (ON/OFF)
- Download my data button (export as JSON/CSV)
- Delete all activity logs button

### 5. Display & UI Settings Section
- Theme selection:
  - Light mode
  - Dark mode
  - Auto (system default)
- Items per page (10, 20, or 50)
- Card/content size preference (small, medium, large)
- Toggle: Show/hide thumbnails

### 6. Recommendation Settings Section
- Transparency: Explain how items are ranked
- Adjust recommendation weights (sliders):
  - Relevance weight (default 0.4)
  - Popularity weight (default 0.3)
  - Recency weight (default 0.3)
- Block content sources (exclude news outlets, YouTube channels)
- Block topics/domains (don't show items from certain interest categories)

### 7. General Settings Section
- Account type selection (Student, Educator, Researcher)
- Bio/About section (optional short bio)
- Avatar/profile picture upload

### 8. Device & Security Section
- View active sessions
- Logout from all devices button

### 9. Help & Support Section
- FAQ link
- Contact support button
- Report a bug link
- Privacy policy link
- Terms & conditions link

---

## 💾 PART 9: DATABASE SCHEMA

### Users Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| email | VARCHAR(UNIQUE) | User's email |
| password_hash | VARCHAR | Hashed password |
| created_at | TIMESTAMP | Account creation |
| updated_at | TIMESTAMP | Last update |
| account_deleted | BOOLEAN | Soft delete |

### UserInterests Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| user_id | Foreign Key | Links to Users |
| interest_domain | VARCHAR | Domain name |
| created_at | TIMESTAMP | When added |

### Items Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| title | VARCHAR | Item title |
| description | TEXT | Full description |
| source_type | ENUM | "video", "news", "article", "research_paper" |
| source_url | VARCHAR | External link |
| thumbnail_url | VARCHAR | Image URL |
| published_date | DATETIME | Publication date |
| content_vector | ARRAY | ML embeddings for similarity |
| view_count | INTEGER | Total views |
| like_count | INTEGER | Total likes |
| save_count | INTEGER | Total saves |
| author | VARCHAR | For papers |
| duration | INTEGER | Video duration in seconds |
| created_at | TIMESTAMP | Added to DB |
| updated_at | TIMESTAMP | Last update |

### ItemTags Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| item_id | Foreign Key | Links to Items |
| tag | VARCHAR | Topic tag (e.g., "AI", "ML") |
| domain | VARCHAR | Associated interest domain |

### UserSearches Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| user_id | Foreign Key | Links to Users |
| query | TEXT | Search keywords |
| searched_at | DATETIME | When searched |
| results_count | INTEGER | Results found |

### UserViews Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| user_id | Foreign Key | Links to Users |
| item_id | Foreign Key | Links to Items |
| view_duration | INTEGER | Seconds spent |
| is_liked | BOOLEAN | Did user like? |
| is_saved | BOOLEAN | Did user save? |
| viewed_at | DATETIME | When viewed |

### UserLikes Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| user_id | Foreign Key | Links to Users |
| item_id | Foreign Key | Links to Items |
| liked_at | DATETIME | When liked |

### UserSaves Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| user_id | Foreign Key | Links to Users |
| item_id | Foreign Key | Links to Items |
| saved_at | DATETIME | When saved |

### UserSettings Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| user_id | Foreign Key | Links to Users |
| theme | ENUM | "light", "dark", "auto" |
| notifications_enabled | BOOLEAN | Toggle notifications |
| notification_frequency | ENUM | "daily", "weekly", "realtime" |
| language | VARCHAR | "en", "hi", etc. |
| items_per_page | INTEGER | Page size |
| relevance_weight | FLOAT | 0.0-1.0 |
| popularity_weight | FLOAT | 0.0-1.0 |
| recency_weight | FLOAT | 0.0-1.0 |
| updated_at | TIMESTAMP | Last update |

### UserBlockedSources Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| user_id | Foreign Key | Links to Users |
| source_name | VARCHAR | News outlet, channel name |
| blocked_at | DATETIME | When blocked |

### UserBlockedDomains Table
| Field | Type | Notes |
|-------|------|-------|
| id | Primary Key | Auto-increment |
| user_id | Foreign Key | Links to Users |
| blocked_domain | VARCHAR | Topic/domain to hide |
| blocked_at | DATETIME | When blocked |

---

## 🔌 PART 10: API ENDPOINTS

### Authentication Endpoints
```
POST /auth/signup
  Input: { email, password }
  Output: { user_id, message, success }

POST /auth/login
  Input: { email, password }
  Output: { token, user_id, message, success }

POST /auth/logout
  Output: { message, success }

POST /auth/change-password
  Input: { old_password, new_password }
  Output: { message, success }
```

### User Profile Endpoints
```
GET /user/profile
  Output: { email, interests, created_at, account_type }

POST /user/interests
  Input: { interests: [domain1, domain2, ...] }
  Output: { message, updated_interests, success }

PUT /user/profile
  Input: { bio, avatar_url, account_type }
  Output: { updated_profile, success }

DELETE /user/account
  Output: { message, confirmation_required, success }
```

### Content & Recommendation Endpoints
```
GET /recommendations?limit=20&offset=0&date_range=week&sort=trending
  Output: { items: [...], total_count, success }

GET /videos?limit=20&offset=0&date_range=week&sort=trending
  Output: { items: [...], total_count, success }

GET /news?limit=20&offset=0&date_range=day&sort=newest
  Output: { items: [...], total_count, success }

GET /articles?limit=20&offset=0&date_range=month&sort=popular
  Output: { items: [...], total_count, success }

GET /books?limit=20&offset=0&sort=relevant
  Output: { items: [...], total_count, success }

GET /search?q=query_string&limit=20&offset=0
  Output: { items: [...], total_count, query, success }

GET /items/{item_id}
  Output: { item_details, related_items, success }
```

### Engagement Tracking Endpoints
```
POST /track/view
  Input: { item_id, view_duration }
  Output: { message, success }

POST /track/like
  Input: { item_id }
  Output: { message, is_liked, success }

POST /track/unlike
  Input: { item_id }
  Output: { message, success }

POST /track/save
  Input: { item_id }
  Output: { message, is_saved, success }

POST /track/unsave
  Input: { item_id }
  Output: { message, success }

POST /search/log
  Input: { query, results_count }
  Output: { message, success }
```

### User Collections Endpoints
```
GET /user/saved-items?limit=20&offset=0
  Output: { items: [...], total_count, success }

GET /user/favorite-items?limit=20&offset=0
  Output: { items: [...], total_count, success }

DELETE /user/saved-items/{item_id}
  Output: { message, success }

DELETE /user/favorite-items/{item_id}
  Output: { message, success }
```

### Settings Endpoints
```
GET /user/settings
  Output: { theme, notifications_enabled, language, ... all settings, success }

PUT /user/settings
  Input: { theme, notifications_enabled, language, ... }
  Output: { updated_settings, success }

PUT /user/settings/recommendation-weights
  Input: { relevance_weight, popularity_weight, recency_weight }
  Output: { message, updated_weights, success }

POST /user/settings/block-source
  Input: { source_name }
  Output: { message, success }

DELETE /user/settings/unblock-source/{source_name}
  Output: { message, success }

POST /user/settings/block-domain
  Input: { domain }
  Output: { message, success }

DELETE /user/settings/unblock-domain/{domain}
  Output: { message, success }

GET /user/settings/data-export
  Output: { download_link or JSON export of all user data, success }
```

---

## 📄 PART 11: ALL PAGES IN THE WEBSITE

| Page Name | Purpose | Key Features |
|-----------|---------|--------------|
| **Landing Page** | Website intro | Info, policies, sign-up CTA |
| **Sign-Up Page** | Create account | Email, password fields |
| **Interest Selection** | Choose interests | Checkboxes for domains |
| **Login Page** | User authentication | Email, password fields |
| **Dashboard/Home** | Main feed | Search, all content mixed, filters |
| **Videos Page** | Video content only | YouTube-style grid layout |
| **Books Page** | Papers & books only | Card layout with cover images |
| **News Page** | News articles only | Wikipedia-style list layout |
| **Articles Page** | Articles only | Medium-style list layout |
| **Item Details Page** | View full item | Full content, related items, like/save |
| **Saved Items Page** | User's bookmarks | Filter, sort, remove from saved |
| **Favorite Items Page** | User's likes | Filter, sort, unlike items |
| **User Profile Page** | Account info | Email, interests, change password, logout, delete account |
| **Settings Page** | Preferences | Account, notifications, privacy, display, recommendations, general, help |

---

## ✅ VERIFICATION CHECKLIST

- ✅ Landing page with info and policies
- ✅ Sign-up with email & password (no username)
- ✅ Interest selection with checkboxes (multiple choice)
- ✅ Login with email & password
- ✅ Dashboard with search bar + left sidebar menu
- ✅ Five menu options: Home, Videos, Books, News, Articles
- ✅ Content display: Videos (YouTube style), News/Articles (Wikipedia style), Papers (card style)
- ✅ Filters: Date range (24h, week, month, all-time)
- ✅ Sorting: Trending, Newest, Most Popular, Most Relevant
- ✅ User engagement: Like, Save, View Full/Read More
- ✅ Recommendation ranking: 40% relevance, 30% popularity, 30% recency
- ✅ User profile page: Email, interests, change password, logout, delete account
- ✅ Saved items page: View & manage saved items
- ✅ Favorite items page: View & manage liked items
- ✅ Settings page: 9 settings sections with detailed options
- ✅ Database: 10 tables with proper relationships
- ✅ API endpoints: 30+ endpoints for all features
- ✅ Tech stack: React + FastAPI + PostgreSQL

---

## 🚀 READY FOR NEXT STEPS?

Is this review correct and complete? Any changes needed?

Once confirmed, what should I build first?
1. Backend (django + Database)
2. Frontend (React pages)
3. Complete code for both

