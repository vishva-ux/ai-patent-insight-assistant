"""
AI Patent Insight Assistant
Streamlit App Entry Point
"""

import streamlit as st
from src.analyzer import PatentAnalyzer
from src.search import SemanticSearch

st.set_page_config(
    page_title="AI Patent Insight Assistant",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 AI Patent Insight Assistant")
st.caption("NLP + LLM-powered patent analysis with semantic search")

tab1, tab2, tab3 = st.tabs(["📄 Analyze Patent", "🔍 Semantic Search", "⚖️ Compare Patents"])

with tab1:
    st.subheader("Paste Patent Text")
    patent_text = st.text_area("Patent content", height=250,
        placeholder="Paste patent abstract, claims, or full document...")
    if st.button("🧠 Analyze", use_container_width=True):
        if patent_text:
            with st.spinner("Analyzing patent..."):
                analyzer = PatentAnalyzer()
                result = analyzer.analyze(patent_text)
            st.success("Analysis complete!")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Executive Summary**")
                st.info(result.get("summary", ""))
                st.markdown("**Core Innovation**")
                st.write(result.get("innovation", ""))
            with col2:
                st.markdown("**Novelty Scores**")
                for k, v in result.get("scores", {}).items():
                    st.progress(v / 100, text=f"{k}: {v}%")
        else:
            st.warning("Please paste patent text first.")

with tab2:
    st.subheader("Semantic Patent Search")
    query = st.text_input("Search query", placeholder="e.g. transformer attention mechanism...")
    if st.button("🔍 Search", use_container_width=True):
        if query:
            with st.spinner("Searching corpus..."):
                searcher = SemanticSearch()
                results = searcher.search(query, top_k=5)
            for r in results:
                with st.expander(f"{r['title']} — sim: {r['score']:.2f}"):
                    st.write(r['excerpt'])
        else:
            st.warning("Please enter a search query.")

with tab3:
    st.subheader("Compare Two Patents")
    col1, col2 = st.columns(2)
    with col1:
        patent_a = st.text_area("Patent A", height=200)
    with col2:
        patent_b = st.text_area("Patent B", height=200)
    if st.button("⚖️ Compare", use_container_width=True):
        if patent_a and patent_b:
            with st.spinner("Computing similarity..."):
                searcher = SemanticSearch()
                score = searcher.compare(patent_a, patent_b)
            st.metric("Semantic Similarity", f"{score:.2f}")
            if score > 0.75:
                st.error("High overlap — potential prior art conflict.")
            elif score > 0.6:
                st.warning("Moderate overlap — review shared claims carefully.")
            else:
                st.success("Low overlap — patents appear sufficiently distinct.")
        else:
            st.warning("Please fill in both patent fields.")
