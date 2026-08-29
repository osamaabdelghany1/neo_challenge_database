INSERT INTO exercises (muscle_id, name, description, equipment_needed, difficulty, video_url) VALUES
-- Biceps Brachii (ID: 1)
(1, 'Barbell Bicep Curl', 'Classic bicep exercise using a barbell for maximum muscle activation', 'Barbell', 'Medium', 'https://example.com/videos/barbell-curl.mp4'),
(1, 'Dumbbell Hammer Curl', 'Targets both biceps and brachialis with neutral grip', 'Dumbbells', 'Easy', 'https://example.com/videos/hammer-curl.mp4'),
(1, 'Concentration Curl', 'Isolation exercise for peak bicep contraction', 'Dumbbell', 'Medium', 'https://example.com/videos/concentration-curl.mp4'),

-- Triceps Brachii (ID: 2)
(2, 'Tricep Pushdown', 'Cable exercise for tricep isolation', 'Cable machine', 'Easy', 'https://example.com/videos/tricep-pushdown.mp4'),
(2, 'Skull Crushers', 'Lying tricep extension using EZ bar or dumbbells', 'EZ bar/Dumbbells', 'Hard', 'https://example.com/videos/skull-crushers.mp4'),
(2, 'Close Grip Bench Press', 'Compound movement for tricep and chest development', 'Barbell and bench', 'Hard', 'https://example.com/videos/close-grip-bench.mp4'),

-- Pectoralis Major (ID: 3)
(3, 'Bench Press', 'Classic chest exercise for overall pectoral development', 'Barbell and bench', 'Medium', 'https://example.com/videos/bench-press.mp4'),
(3, 'Incline Dumbbell Press', 'Targets upper chest for fuller appearance', 'Dumbbells and incline bench', 'Medium', 'https://example.com/videos/incline-press.mp4'),
(3, 'Cable Fly', 'Isolation exercise for chest definition', 'Cable machine', 'Easy', 'https://example.com/videos/cable-fly.mp4'),

-- Latissimus Dorsi (ID: 4)
(4, 'Pull Up', 'Bodyweight exercise for back width and strength', 'Pull up bar', 'Hard', 'https://example.com/videos/pull-up.mp4'),
(4, 'Lat Pulldown', 'Machine alternative to pull ups for back development', 'Cable machine', 'Medium', 'https://example.com/videos/lat-pulldown.mp4'),
(4, 'Bent Over Row', 'Free weight exercise for back thickness', 'Barbell', 'Hard', 'https://example.com/videos/bent-row.mp4'),

-- Deltoids (ID: 5)
(5, 'Overhead Press', 'Compound movement for overall shoulder development', 'Barbell/Dumbbells', 'Hard', 'https://example.com/videos/overhead-press.mp4'),
(5, 'Lateral Raise', 'Isolation exercise for side deltoids', 'Dumbbells', 'Easy', 'https://example.com/videos/lateral-raise.mp4'),
(5, 'Front Raise', 'Targets anterior deltoids for shoulder definition', 'Dumbbells/Barbell', 'Easy', 'https://example.com/videos/front-raise.mp4'),

-- Rectus Abdominis (ID: 6)
(6, 'Crunch', 'Basic ab exercise for upper rectus abdominis', 'None', 'Easy', 'https://example.com/videos/crunch.mp4'),
(6, 'Leg Raise', 'Targets lower abs and hip flexors', 'None', 'Medium', 'https://example.com/videos/leg-raise.mp4'),
(6, 'Plank', 'Isometric exercise for core stability', 'None', 'Medium', 'https://example.com/videos/plank.mp4'),

-- Obliques (ID: 7)
(7, 'Russian Twist', 'Rotational exercise for oblique development', 'None/Weight', 'Medium', 'https://example.com/videos/russian-twist.mp4'),
(7, 'Side Plank', 'Isometric exercise for oblique strength', 'None', 'Hard', 'https://example.com/videos/side-plank.mp4'),
(7, 'Cable Woodchop', 'Functional rotational movement for obliques', 'Cable machine', 'Medium', 'https://example.com/videos/woodchop.mp4'),

-- Quadriceps Femoris (ID: 8)
(8, 'Squat', 'King of leg exercises for quad development', 'Barbell/Squat rack', 'Hard', 'https://example.com/videos/squat.mp4'),
(8, 'Leg Press', 'Machine exercise for heavy quad loading', 'Leg press machine', 'Medium', 'https://example.com/videos/leg-press.mp4'),
(8, 'Lunge', 'Unilateral exercise for quad strength and balance', 'None/Dumbbells', 'Medium', 'https://example.com/videos/lunge.mp4'),

-- Hamstrings (ID: 9)
(9, 'Romanian Deadlift', 'Targets hamstrings and glutes with hip hinge', 'Barbell', 'Hard', 'https://example.com/videos/rdl.mp4'),
(9, 'Leg Curl', 'Isolation exercise for hamstring development', 'Leg curl machine', 'Easy', 'https://example.com/videos/leg-curl.mp4'),
(9, 'Glute Bridge', 'Bodyweight exercise for hamstrings and glutes', 'None', 'Easy', 'https://example.com/videos/glute-bridge.mp4'),

-- Gastrocnemius (ID: 10)
(10, 'Standing Calf Raise', 'Targets gastrocnemius with straight leg', 'Calf raise machine', 'Easy', 'https://example.com/videos/standing-calf.mp4'),
(10, 'Jump Rope', 'Dynamic exercise for calf endurance', 'Jump rope', 'Medium', 'https://example.com/videos/jump-rope.mp4'),
(10, 'Box Jumps', 'Plyometric exercise for explosive calf power', 'Plyo box', 'Hard', 'https://example.com/videos/box-jump.mp4'),

-- Gluteus Maximus (ID: 11)
(11, 'Hip Thrust', 'Isolation exercise for glute maximus', 'Bench and barbell', 'Medium', 'https://example.com/videos/hip-thrust.mp4'),
(11, 'Sumo Deadlift', 'Wide stance deadlift for glute activation', 'Barbell', 'Hard', 'https://example.com/videos/sumo-dl.mp4'),
(11, 'Bulgarian Split Squat', 'Unilateral exercise for glute development', 'Bench and dumbbells', 'Hard', 'https://example.com/videos/bulgarian-split.mp4'),

-- Trapezius (ID: 12)
(12, 'Shrug', 'Direct trap exercise for upper trap development', 'Barbell/Dumbbells', 'Easy', 'https://example.com/videos/shrug.mp4'),
(12, 'Face Pull', 'Targets rear delts and mid traps', 'Cable machine', 'Medium', 'https://example.com/videos/face-pull.mp4'),
(12, 'Upright Row', 'Compound movement for trap and shoulder development', 'Barbell/Dumbbells', 'Medium', 'https://example.com/videos/upright-row.mp4'),

-- Rhomboids (ID: 13)
(13, 'Scapular Retraction', 'Isolation exercise for rhomboid activation', 'Cable machine', 'Easy', 'https://example.com/videos/scap-retraction.mp4'),
(13, 'Reverse Fly', 'Targets rear delts and rhomboids', 'Dumbbells/Cable', 'Medium', 'https://example.com/videos/reverse-fly.mp4'),
(13, 'Seated Row', 'Compound exercise for back and rhomboid development', 'Cable machine', 'Medium', 'https://example.com/videos/seated-row.mp4'),

-- Erector Spinae (ID: 14)
(14, 'Back Extension', 'Bodyweight exercise for lower back strength', 'Hyperextension bench', 'Easy', 'https://example.com/videos/back-extension.mp4'),
(14, 'Good Morning', 'Advanced exercise for erector spinae development', 'Barbell', 'Hard', 'https://example.com/videos/good-morning.mp4'),
(14, 'Superman Hold', 'Bodyweight isometric for lower back', 'None', 'Medium', 'https://example.com/videos/superman.mp4'),

-- Soleus (ID: 15)
(15, 'Seated Calf Raise', 'Targets soleus with bent knee', 'Calf raise machine', 'Easy', 'https://example.com/videos/seated-calf.mp4'),
(15, 'Donkey Calf Raise', 'Old school exercise for soleus development', 'None/Weight', 'Medium', 'https://example.com/videos/donkey-calf.mp4'),
(15, 'Tibialis Raise', 'Anterior tibialis exercise for balanced calf development', 'None/Weight', 'Medium', 'https://example.com/videos/tibialis-raise.mp4');