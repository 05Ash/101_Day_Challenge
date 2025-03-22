--
-- PostgreSQL database dump
--

-- Dumped from database version 12.17 (Ubuntu 12.17-1.pgdg22.04+1)
-- Dumped by pg_dump version 12.17 (Ubuntu 12.17-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    galaxy_id integer NOT NULL,
    name character varying(40) NOT NULL,
    galaxy_code character varying(10),
    galaxy_type character varying(20),
    estimated_age_in_billion numeric(5,2),
    distance_from_earth_in_million_light_years numeric(6,3)
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.galaxy_galaxy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galaxy_galaxy_id_seq OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.galaxy_galaxy_id_seq OWNED BY public.galaxy.galaxy_id;


--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    moon_id integer NOT NULL,
    name character varying(30) NOT NULL,
    orbital_period_in_days numeric(5,2),
    features text,
    planet_id integer
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.moon_moon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moon_moon_id_seq OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.moon_moon_id_seq OWNED BY public.moon.moon_id;


--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    planet_id integer NOT NULL,
    name character varying(30) NOT NULL,
    num_of_moons integer,
    is_habitable boolean,
    orbital_period_in_days numeric(10,2),
    star_id integer
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.planet_planet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planet_planet_id_seq OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.planet_planet_id_seq OWNED BY public.planet.planet_id;


--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    star_id integer NOT NULL,
    name character varying(40) NOT NULL,
    type character varying(50),
    num_of_planets_found integer,
    galaxy_id integer,
    star_system_id integer
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.star_star_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.star_star_id_seq OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.star_star_id_seq OWNED BY public.star.star_id;


--
-- Name: star_system; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star_system (
    star_system_id integer NOT NULL,
    name character varying(40) NOT NULL,
    num_of_suns integer,
    num_of_planets integer,
    is_habitable boolean,
    notes text,
    galaxy_id integer NOT NULL
);


ALTER TABLE public.star_system OWNER TO freecodecamp;

--
-- Name: star_systems_star_system_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.star_systems_star_system_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.star_systems_star_system_id_seq OWNER TO freecodecamp;

--
-- Name: star_systems_star_system_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.star_systems_star_system_id_seq OWNED BY public.star_system.star_system_id;


--
-- Name: galaxy galaxy_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy ALTER COLUMN galaxy_id SET DEFAULT nextval('public.galaxy_galaxy_id_seq'::regclass);


--
-- Name: moon moon_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon ALTER COLUMN moon_id SET DEFAULT nextval('public.moon_moon_id_seq'::regclass);


--
-- Name: planet planet_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet ALTER COLUMN planet_id SET DEFAULT nextval('public.planet_planet_id_seq'::regclass);


--
-- Name: star star_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star ALTER COLUMN star_id SET DEFAULT nextval('public.star_star_id_seq'::regclass);


--
-- Name: star_system star_system_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star_system ALTER COLUMN star_system_id SET DEFAULT nextval('public.star_systems_star_system_id_seq'::regclass);


--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES (1, 'Mlky Way', NULL, 'Barred Spiral', 13.60, 0.026);
INSERT INTO public.galaxy VALUES (2, 'Andromeda', 'M31', 'Spiral', 10.00, 2.540);
INSERT INTO public.galaxy VALUES (3, 'Triangulum', 'M33', 'Spiral', 12.00, 2.730);
INSERT INTO public.galaxy VALUES (4, 'Whirlpool', 'M51', 'Spiral', 10.00, 23.000);
INSERT INTO public.galaxy VALUES (5, 'Sombrero', 'M104', 'Lentucular', 9.50, 29.300);
INSERT INTO public.galaxy VALUES (6, 'Messier 87', 'M87', 'Elliptical', 13.20, 53.500);
INSERT INTO public.galaxy VALUES (7, 'Large Magellanic Cloud', 'LMC', 'Irregular', 3.00, 0.162);
INSERT INTO public.galaxy VALUES (8, 'Small Magellanic Cloud', 'SMC', 'Irregular', 6.00, 0.199);
INSERT INTO public.galaxy VALUES (9, 'Centaurus A', 'NGC 5128', 'Elliptical', 16.00, 12.000);
INSERT INTO public.galaxy VALUES (10, 'NGC 1300', 'NGC 1300', 'Barred Spiral', 10.00, 61.300);


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES (1, 'Moon', 27.30, 'Only natural satellite of Earth, controls tides', 3);
INSERT INTO public.moon VALUES (2, 'Phobos', 0.32, 'Orbits closer than any other moon in the Solar System', 4);
INSERT INTO public.moon VALUES (3, 'Deimos', 1.26, 'Small and irregular, possibly a captured asteroid', 4);
INSERT INTO public.moon VALUES (4, 'Io', 1.77, 'Most volcanically active body in the Solar System', 5);
INSERT INTO public.moon VALUES (5, 'Europa', 3.55, 'Subsurface ocean, potential for life', 5);
INSERT INTO public.moon VALUES (6, 'Ganumede', 7.15, 'Largest moon in the Solar System', 5);
INSERT INTO public.moon VALUES (7, 'Callisto', 16.69, 'Heavily cratered, may have a subsurface ocean', 5);
INSERT INTO public.moon VALUES (8, 'Titan', 15.94, 'Thick atmosphere, lakes of liquid methane', 6);
INSERT INTO public.moon VALUES (9, 'Enceladus', 1.37, 'Ice-covered, water plumes, potential for life', 6);
INSERT INTO public.moon VALUES (10, 'Mimas', 0.94, '"Death Star" moon due to massive crater', 6);
INSERT INTO public.moon VALUES (11, 'Triton', 5.88, 'Orbits in retrograde, possible captured dwarf planet', 8);
INSERT INTO public.moon VALUES (12, 'Miranda', 1.41, 'Bizarre surface, extreme geological activity', 7);
INSERT INTO public.moon VALUES (13, 'Oberon', 13.46, 'Second largest Uranian moon, icy and rocky', 7);
INSERT INTO public.moon VALUES (14, 'Iapetus', 79.33, 'Two-tone coloration, one side dark, one bright', 6);
INSERT INTO public.moon VALUES (15, 'Proxima b Moon', NULL, 'Possibly tidally locked, data uncertain', 9);
INSERT INTO public.moon VALUES (16, 'Gliese 581g Moon', NULL, 'Might have thick atmosphere', 11);
INSERT INTO public.moon VALUES (17, 'Trappist-1e Moon', NULL, 'Could have liquid water', 13);
INSERT INTO public.moon VALUES (18, 'Kepler-442b Moon', NULL, 'Potentially habitable', 15);
INSERT INTO public.moon VALUES (19, 'TOI-700 d Moon', NULL, 'In the habitable zone', 21);
INSERT INTO public.moon VALUES (20, 'Kapteyn b Moon', NULL, 'Ancient exoplanet, possible rocky moon', 18);


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES (1, 'Mercury', 0, false, 88.00, 1);
INSERT INTO public.planet VALUES (2, 'Venus', 0, false, 225.00, 1);
INSERT INTO public.planet VALUES (3, 'Earth', 1, true, 365.25, 1);
INSERT INTO public.planet VALUES (4, 'Mars', 2, false, 687.00, 1);
INSERT INTO public.planet VALUES (5, 'Jupiter', 95, false, 4332.00, 1);
INSERT INTO public.planet VALUES (6, 'Saturn', 146, false, 10759.00, 1);
INSERT INTO public.planet VALUES (7, 'Uranus', 27, false, 30687.00, 1);
INSERT INTO public.planet VALUES (8, 'Neptune', 14, false, 60190.00, 1);
INSERT INTO public.planet VALUES (9, 'Proxima b', NULL, true, 11.20, 4);
INSERT INTO public.planet VALUES (10, 'Proxima C', NULL, false, 1880.00, 4);
INSERT INTO public.planet VALUES (11, 'Gliese 581g', NULL, true, 30.00, 7);
INSERT INTO public.planet VALUES (12, 'Gliese 581c', NULL, false, 13.00, 7);
INSERT INTO public.planet VALUES (13, 'Trappist-1e', NULL, true, 6.10, 10);
INSERT INTO public.planet VALUES (14, 'Trappist-1f', NULL, true, 9.20, 10);
INSERT INTO public.planet VALUES (15, 'Keppler-442b', NULL, true, 112.00, 9);
INSERT INTO public.planet VALUES (16, 'HD 209458 b', NULL, false, 3.50, 8);
INSERT INTO public.planet VALUES (17, 'Tau Ceti e', NULL, true, 163.00, 11);
INSERT INTO public.planet VALUES (18, 'Kapteyn b', NULL, true, 48.00, 12);
INSERT INTO public.planet VALUES (19, 'Wolf 1061c', NULL, true, 17.90, 15);
INSERT INTO public.planet VALUES (20, 'Ross 128 b', NULL, true, 9.90, 17);
INSERT INTO public.planet VALUES (21, 'TOI-700 d', NULL, true, 37.40, 23);


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES (1, 'Sun', 'G-type Main Sequence', 8, 1, 1);
INSERT INTO public.star VALUES (2, 'Alpha Centauri A', 'G-type Main Sequence', 3, 1, 2);
INSERT INTO public.star VALUES (3, 'Alpha Centauri B', 'K-type Main Sequence', 3, 1, 2);
INSERT INTO public.star VALUES (4, 'Proxima Centauri', 'Red Dwarf', 3, 1, 2);
INSERT INTO public.star VALUES (5, 'Zeta Reticuli A', 'G-type Main Sequence', 2, 2, 3);
INSERT INTO public.star VALUES (6, 'Zeta Reticuli B', 'G-type Main Sequence', 2, 2, 3);
INSERT INTO public.star VALUES (7, 'Gliese 581', 'Red Dwarf', 4, 2, 4);
INSERT INTO public.star VALUES (8, 'HD 209458', 'G-type Main Sequence', 2, 3, 5);
INSERT INTO public.star VALUES (9, 'Keppler-442', 'K-type Main Sequence', 1, 3, 6);
INSERT INTO public.star VALUES (10, 'Trappist-1', 'Red Dwarf', 7, 4, 7);
INSERT INTO public.star VALUES (11, 'Tau Ceti', 'G-type Main Sequence', 4, 5, 9);
INSERT INTO public.star VALUES (12, 'Kapteyn’s Star', 'Red Dwarf', 2, 5, 10);
INSERT INTO public.star VALUES (13, 'Vega', 'A-type Main Sequence', 2, 6, 11);
INSERT INTO public.star VALUES (14, 'Barnard''s Star', 'Red Dwarf', 1, 6, 12);
INSERT INTO public.star VALUES (15, 'Wolf 1061', 'Red Dwarf', 1, 7, 13);
INSERT INTO public.star VALUES (16, 'Epsilon Eridani', 'K-type Main Sequence', 2, 7, 14);
INSERT INTO public.star VALUES (17, 'Ross 128', 'Red Dwarf', 1, 8, 15);
INSERT INTO public.star VALUES (18, 'Gliese 876', 'Red Dwarf', 4, 8, 16);
INSERT INTO public.star VALUES (19, 'HD 40307', 'K-type Main Sequence', 3, 9, 17);
INSERT INTO public.star VALUES (20, 'Kepler-22', 'G-type Main Sequence', 1, 9, 18);
INSERT INTO public.star VALUES (21, '55 Cancri A', 'G-type Main Sequence', 5, 10, 19);
INSERT INTO public.star VALUES (22, '55 Cancri B', 'Red Dwarf', 5, 10, 19);
INSERT INTO public.star VALUES (23, 'TOI-700', 'Red Dwarf', 3, 10, 20);


--
-- Data for Name: star_system; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star_system VALUES (1, 'Solar System', 1, 8, true, 'Home to Earth, Mars has potential', 1);
INSERT INTO public.star_system VALUES (2, 'Alpha Centauri System', 3, 2, true, 'Closest exoplanet to Earth', 1);
INSERT INTO public.star_system VALUES (3, 'Zeta Reticuli System', 2, 1, true, 'Theorized for advanced life', 2);
INSERT INTO public.star_system VALUES (4, 'Gliese 581 System', 1, 4, true, 'One of the earliest discovered exoplanets discovered in the habitable zone', 2);
INSERT INTO public.star_system VALUES (5, 'HD 209458 Stystem', 1, 4, false, 'HD 209458 b is a "Hot Jupiter"', 3);
INSERT INTO public.star_system VALUES (6, 'Kepler-442 System', 1, 1, true, 'A promising super-Earth candidate', 3);
INSERT INTO public.star_system VALUES (7, 'Tappist System', 1, 7, true, 'Multiple Earth-like exoplanets', 4);
INSERT INTO public.star_system VALUES (8, 'LHS 1140 System', 1, 2, true, 'Large rocky expoplanet in habitable zone', 4);
INSERT INTO public.star_system VALUES (9, 'Tau Ceti System', 1, 4, false, 'Presence of debris disks, making habitablility uncertain', 5);
INSERT INTO public.star_system VALUES (10, 'Kapteyn''s System', 1, 2, true, 'One of the oldest habitable exoplanets', 5);
INSERT INTO public.star_system VALUES (11, 'Vega System', 1, 2, false, 'High radiation levels', 6);
INSERT INTO public.star_system VALUES (12, 'Barnard''s System', 1, 1, true, 'Barnard''s Star b is cold but might have a subsurface ocean', 6);
INSERT INTO public.star_system VALUES (13, 'Wolf 1061 System', 1, 3, true, 'Near the inner edge of the habitable zone', 7);
INSERT INTO public.star_system VALUES (14, 'Epsilon Eridani System', 1, 2, true, 'Has a debris disk like the early Solar System', 7);
INSERT INTO public.star_system VALUES (15, 'Ross 128 System', 1, 1, true, 'One of the closest habitable exoplanets', 8);
INSERT INTO public.star_system VALUES (16, 'Gliese 876 System', 1, 4, true, 'Small Neptune-like planet in habitable zone', 8);
INSERT INTO public.star_system VALUES (17, 'HD 40307 System', 1, 3, true, 'Super-Earth with potential for liquid water', 9);
INSERT INTO public.star_system VALUES (18, 'Keppler-22 System', 1, 1, true, 'A strong candidate for life', 9);
INSERT INTO public.star_system VALUES (19, '55 Cancri System', 1, 5, true, 'Super Earth with unknown atmosphere', 10);
INSERT INTO public.star_system VALUES (20, 'TOI-700 System', 1, 3, true, 'One of NASA''s best habitable zone discoveries', 10);


--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.galaxy_galaxy_id_seq', 10, true);


--
-- Name: moon_moon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.moon_moon_id_seq', 20, true);


--
-- Name: planet_planet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.planet_planet_id_seq', 21, true);


--
-- Name: star_star_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.star_star_id_seq', 23, true);


--
-- Name: star_systems_star_system_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.star_systems_star_system_id_seq', 20, true);


--
-- Name: galaxy galaxy_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_name_key UNIQUE (name);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: moon moon_moon_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_moon_name_key UNIQUE (name);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: planet planet_planet_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_planet_name_key UNIQUE (name);


--
-- Name: star star_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_name_key UNIQUE (name);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: star_system star_systems_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star_system
    ADD CONSTRAINT star_systems_name_key UNIQUE (name);


--
-- Name: star_system star_systems_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star_system
    ADD CONSTRAINT star_systems_pkey PRIMARY KEY (star_system_id);


--
-- Name: moon moon_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: planet planet_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: star star_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- Name: star star_star_system_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_star_system_id_fkey FOREIGN KEY (star_system_id) REFERENCES public.star_system(star_system_id);


--
-- Name: star_system star_systems_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star_system
    ADD CONSTRAINT star_systems_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--

