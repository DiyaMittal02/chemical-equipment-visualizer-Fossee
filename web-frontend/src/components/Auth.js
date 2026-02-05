import React, { useState } from 'react';
import { loginUser, registerUser } from '../api';

function Auth({ onLoginSuccess }) {
    const [isLogin, setIsLogin] = useState(true);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setSuccess('');
        setLoading(true);

        try {
            if (isLogin) {
                const userData = await loginUser(username, password);
                setSuccess('Login successful!');
                onLoginSuccess(userData);
            } else {
                await registerUser(username, password, email);
                setSuccess('Registration successful! Please login.');
                setIsLogin(true);
                setPassword('');
            }
        } catch (err) {
            setError(err.response?.data?.error || err.message || 'An error occurred. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-gray-800/60 backdrop-blur-lg rounded-2xl border border-gray-700 p-8 shadow-2xl">
            <div className="text-center mb-8">
                <div className="text-5xl mb-4">{isLogin ? '🔐' : '✨'}</div>
                <h2 className="text-3xl font-bold text-white mb-2">
                    {isLogin ? 'Sign In' : 'Create Account'}
                </h2>
                <p className="text-gray-400">
                    {isLogin
                        ? 'Welcome back! Sign in to access your equipment data.'
                        : 'Join us to start analyzing your equipment parameters.'}
                </p>
            </div>

            {error && (
                <div className="mb-4 p-4 bg-red-500/10 border border-red-500/50 rounded-lg flex items-center gap-3 text-red-400">
                    <span className="text-xl">⚠️</span>
                    <span>{error}</span>
                </div>
            )}

            {success && (
                <div className="mb-4 p-4 bg-green-500/10 border border-green-500/50 rounded-lg flex items-center gap-3 text-green-400">
                    <span className="text-xl">✅</span>
                    <span>{success}</span>
                </div>
            )}

            <form onSubmit={handleSubmit} className="space-y-5">
                <div>
                    <label htmlFor="username" className="block text-sm font-medium text-gray-300 mb-2">
                        Username
                    </label>
                    <input
                        id="username"
                        type="text"
                        className="w-full px-4 py-3 bg-gray-900/50 border border-gray-600 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        placeholder="Enter your username"
                        required
                    />
                </div>

                {!isLogin && (
                    <div>
                        <label htmlFor="email" className="block text-sm font-medium text-gray-300 mb-2">
                            Email (Optional)
                        </label>
                        <input
                            id="email"
                            type="email"
                            className="w-full px-4 py-3 bg-gray-900/50 border border-gray-600 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="Enter your email"
                        />
                    </div>
                )}

                <div>
                    <label htmlFor="password" className="block text-sm font-medium text-gray-300 mb-2">
                        Password
                    </label>
                    <input
                        id="password"
                        type="password"
                        className="w-full px-4 py-3 bg-gray-900/50 border border-gray-600 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Enter your password"
                        required
                    />
                </div>

                <button
                    type="submit"
                    className="w-full py-3 px-4 bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-700 hover:to-blue-600 text-white font-semibold rounded-lg shadow-lg shadow-blue-500/50 hover:shadow-blue-500/70 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                    disabled={loading}
                >
                    {loading ? (
                        <>
                            <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
                            Processing...
                        </>
                    ) : (
                        isLogin ? 'Sign In' : 'Create Account'
                    )}
                </button>
            </form>

            <div className="mt-6 text-center">
                <p className="text-gray-400">
                    {isLogin ? "Don't have an account? " : "Already have an account? "}
                    <button
                        type="button"
                        onClick={() => {
                            setIsLogin(!isLogin);
                            setError('');
                            setSuccess('');
                        }}
                        className="text-blue-400 hover:text-blue-300 font-semibold transition-colors"
                    >
                        {isLogin ? 'Sign Up' : 'Sign In'}
                    </button>
                </p>
            </div>
        </div>
    );
}

export default Auth;
